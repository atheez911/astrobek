/*
 * Koinot Sayohati — sayyoralarni haqiqiy (fotorealistik) teksturalar bilan
 * chizadigan modul. Barcha rasm fayllari loyiha ichida (static/astronomy/img/)
 * saqlanadi, shuning uchun internetga ulanmasdan ham to'liq ishlaydi.
 */

(function (global) {
  'use strict';

  var textureLoader = new THREE.TextureLoader();
  var textureCache = {};

  function loadTex(filename) {
    if (!filename) return null;
    if (textureCache[filename]) return textureCache[filename];
    var url = (global.ASTRO_IMG_BASE || '/static/astronomy/img/') + filename;
    var tex = textureLoader.load(url);
    if ('colorSpace' in tex && THREE.SRGBColorSpace) tex.colorSpace = THREE.SRGBColorSpace;
    textureCache[filename] = tex;
    return tex;
  }

  /* ---------- Yulduzlar foni (3D sahna ichida) ---------- */
  function makeStarfield(scene, count) {
    var geometry = new THREE.BufferGeometry();
    var positions = new Float32Array(count * 3);
    var colors = new Float32Array(count * 3);
    for (var i = 0; i < count; i++) {
      var radius = 220 + Math.random() * 380;
      var theta = Math.random() * Math.PI * 2;
      var phi = Math.acos((Math.random() * 2) - 1);
      positions[i * 3] = radius * Math.sin(phi) * Math.cos(theta);
      positions[i * 3 + 1] = radius * Math.sin(phi) * Math.sin(theta);
      positions[i * 3 + 2] = radius * Math.cos(phi);
      var b = 0.6 + Math.random() * 0.4;
      colors[i * 3] = b;
      colors[i * 3 + 1] = b;
      colors[i * 3 + 2] = Math.min(1, b + Math.random() * 0.2);
    }
    geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
    var material = new THREE.PointsMaterial({ size: 1.1, vertexColors: true, transparent: true, opacity: 0.9, sizeAttenuation: true });
    var points = new THREE.Points(geometry, material);
    scene.add(points);
    return points;
  }

  /* halqa donut-shaklidagi (allaqachon shaffof) rasm bo'lgani uchun
     uni tekis, planet markazidan o'tuvchi disk ustiga proyeksiya qilamiz */
  function ringPlaneSize(kind) {
    // o'lchamlar rasm ichidagi teshik nisbatiga qarab hisoblangan
    if (kind === 'saturn_ring.png') return 1.3 / 0.606 * 2; // ~4.29
    if (kind === 'uranus_ring.png') return 1.3 / 0.694 * 2; // ~3.75
    return 4.2;
  }

  /* ---------- Asosiy funksiya: sahnani yaratish ---------- */

  global.initPlanetScene = function (container, opts) {
    opts = opts || {};
    var textureFile = opts.texture;
    var ringTextureFile = opts.ringTexture || null;
    var interactive = opts.interactive !== false;
    var compact = !!opts.compact;
    var withMoon = !!opts.withMoon;
    var cloudsAlpha = opts.cloudsAlpha || null;
    var autoRotateSpeed = (typeof opts.autoRotateSpeed === 'number') ? opts.autoRotateSpeed : 0.003;
    var axialTilt = (typeof opts.axialTilt === 'number') ? opts.axialTilt : 0.05;

    if (!container || typeof THREE === 'undefined') return null;

    var width = container.clientWidth || 300;
    var height = container.clientHeight || (compact ? width : 420);
    if (!compact && height < 300) height = 420;

    var scene = new THREE.Scene();
    var camera = new THREE.PerspectiveCamera(42, width / height, 0.1, 2000);
    camera.position.set(0, compact ? 0.15 : 0.6, compact ? 3.2 : 4.4);

    var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.setSize(width, height);
    container.innerHTML = '';
    container.appendChild(renderer.domElement);

    // yorug'lik: "quyosh" nuqta manbasi + yumshoq ambient
    var sun = new THREE.PointLight(0xffffff, 2.1, 0, 0);
    sun.position.set(5, 2, 5);
    scene.add(sun);
    scene.add(new THREE.AmbientLight(0x404060, compact ? 1.2 : 0.62));

    if (!compact) makeStarfield(scene, 900);

    var tiltGroup = new THREE.Group();
    tiltGroup.rotation.z = axialTilt;
    scene.add(tiltGroup);

    var planetGroup = new THREE.Group();
    tiltGroup.add(planetGroup);

    var texture = loadTex(textureFile);
    var geometry = new THREE.SphereGeometry(1.3, 56, 56);
    var material = new THREE.MeshPhongMaterial({ map: texture, shininess: cloudsAlpha ? 10 : 3 });
    var planet = new THREE.Mesh(geometry, material);
    planetGroup.add(planet);

    var clouds = null;
    if (cloudsAlpha) {
      var cloudGeo = new THREE.SphereGeometry(1.315, 56, 56);
      var cloudMat = new THREE.MeshPhongMaterial({
        color: 0xffffff,
        alphaMap: loadTex(cloudsAlpha),
        transparent: true,
        opacity: 0.85,
        depthWrite: false
      });
      clouds = new THREE.Mesh(cloudGeo, cloudMat);
      planetGroup.add(clouds);
    }

    var ringMesh = null;
    if (ringTextureFile) {
      var ringSize = ringPlaneSize(ringTextureFile);
      var ringGeo = new THREE.PlaneGeometry(ringSize, ringSize);
      var ringMat = new THREE.MeshBasicMaterial({
        map: loadTex(ringTextureFile),
        transparent: true,
        alphaTest: 0.02,
        side: THREE.DoubleSide,
        depthWrite: false
      });
      ringMesh = new THREE.Mesh(ringGeo, ringMat);
      ringMesh.rotation.x = -Math.PI / 2;
      tiltGroup.add(ringMesh);
    }

    var moonMesh = null, moonAngle = Math.random() * Math.PI * 2;
    if (withMoon) {
      var moonTex = loadTex('moon.jpg');
      var moonGeo = new THREE.SphereGeometry(0.32, 28, 28);
      var moonMat = new THREE.MeshPhongMaterial({ map: moonTex });
      moonMesh = new THREE.Mesh(moonGeo, moonMat);
      scene.add(moonMesh);
    }

    var controls = null;
    if (interactive && THREE.OrbitControls) {
      controls = new THREE.OrbitControls(camera, renderer.domElement);
      controls.enableDamping = true;
      controls.dampingFactor = 0.08;
      controls.minDistance = 2.2;
      controls.maxDistance = compact ? 6 : 9;
      controls.enablePan = false;
      controls.autoRotate = false;
    }

    function resize() {
      var w = container.clientWidth || width;
      var h = compact ? w : (container.clientHeight || height);
      camera.aspect = w / h;
      camera.updateProjectionMatrix();
      renderer.setSize(w, h);
    }

    if (window.ResizeObserver) {
      new ResizeObserver(resize).observe(container);
    } else {
      window.addEventListener('resize', resize);
    }

    var clock = new THREE.Clock();

    function animate() {
      requestAnimationFrame(animate);
      var dt = Math.min(clock.getDelta(), 0.05);
      planet.rotation.y += autoRotateSpeed * 60 * dt;
      if (clouds) clouds.rotation.y += autoRotateSpeed * 26 * dt;
      if (moonMesh) {
        moonAngle += 0.35 * dt;
        moonMesh.position.set(Math.cos(moonAngle) * 2.3, Math.sin(moonAngle * 0.6) * 0.3, Math.sin(moonAngle) * 2.3);
        moonMesh.rotation.y += 0.4 * dt;
      }
      if (controls) controls.update();
      renderer.render(scene, camera);
    }
    animate();

    return { scene: scene, camera: camera, renderer: renderer, planet: planet };
  };

})(window);

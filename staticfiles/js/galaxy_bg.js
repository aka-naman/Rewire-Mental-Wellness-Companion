// Galaxy background for all pages using Three.js
(function() {
    if (!window.THREE) {
        // Wait for Three.js to load
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js';
        script.onload = initGalaxyBG;
        document.head.appendChild(script);
    } else {
        initGalaxyBG();
    }

    function initGalaxyBG() {
        if (document.getElementById('galaxy-bg-canvas')) return;
        const canvas = document.createElement('canvas');
        canvas.id = 'galaxy-bg-canvas';
        canvas.style.position = 'fixed';
        canvas.style.top = 0;
        canvas.style.left = 0;
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.zIndex = '-1';
        canvas.style.pointerEvents = 'none';
        canvas.style.background = 'transparent';
        document.body.appendChild(canvas);

        const renderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
        renderer.setClearColor(0x000010, 1);
        renderer.setSize(window.innerWidth, window.innerHeight);

        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
        camera.position.z = 30;

        // Galaxy/starfield effect
        const starCount = 2000;
        const geometry = new THREE.BufferGeometry();
        const positions = [];
        const colors = [];
        // Theme star colors
        const starColors = [
            new THREE.Color('#d4c5ff'),
            new THREE.Color('#bfbfff'),
            new THREE.Color('#9fb2ff'),
            new THREE.Color('#6C5DD3')
        ];
        for (let i = 0; i < starCount; i++) {
            const r = 60 * Math.pow(Math.random(), 0.7);
            const theta = Math.random() * 2 * Math.PI;
            const phi = Math.acos(2 * Math.random() - 1);
            const x = r * Math.sin(phi) * Math.cos(theta);
            const y = r * Math.sin(phi) * Math.sin(theta);
            const z = r * Math.cos(phi);
            positions.push(x, y, z);
            // Use theme colors for particles
            const color = starColors[Math.floor(Math.random() * starColors.length)];
            colors.push(color.r, color.g, color.b);
        }
        geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
        const material = new THREE.PointsMaterial({ size: 0.25, vertexColors: true });
        const stars = new THREE.Points(geometry, material);
        scene.add(stars);

        function animate() {
            requestAnimationFrame(animate);
            stars.rotation.y += 0.0008;
            stars.rotation.x += 0.0002;
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', function() {
            renderer.setSize(window.innerWidth, window.innerHeight);
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.updateProjectionMatrix();
        });
    }
})();

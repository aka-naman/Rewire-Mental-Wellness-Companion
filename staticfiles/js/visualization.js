// Three.js Visualization for Rewire App

// Initialize the visualization when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function() {
    // Check if the visualization container exists on the current page
    const container = document.getElementById('visualization');
    if (!container) return;
    
    // Set up the scene, camera, and renderer
    const scene = new THREE.Scene();
    // Galaxy/starfield background setup
    const camera = new THREE.PerspectiveCamera(75, container.clientWidth / container.clientHeight, 0.1, 1000);
    camera.position.z = 5;

    const renderer = new THREE.WebGLRenderer({ antialias: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);

    // Responsive behavior
    window.addEventListener('resize', function() {
        camera.aspect = container.clientWidth / container.clientHeight;
        camera.updateProjectionMatrix();
        renderer.setSize(container.clientWidth, container.clientHeight);
    });

    // Galaxy/starfield effect
    const starCount = 2000;
    const geometry = new THREE.BufferGeometry();
    const positions = [];
    const colors = [];
    for (let i = 0; i < starCount; i++) {
        const r = 20 * Math.pow(Math.random(), 0.7); // denser center
        const theta = Math.random() * 2 * Math.PI;
        const phi = Math.acos(2 * Math.random() - 1);
        const x = r * Math.sin(phi) * Math.cos(theta);
        const y = r * Math.sin(phi) * Math.sin(theta);
        const z = r * Math.cos(phi);
        positions.push(x, y, z);
        // Color: white with slight blue/purple tint
        const color = new THREE.Color().setHSL(0.65 + 0.1 * Math.random(), 0.7, 0.8 + 0.2 * Math.random());
        colors.push(color.r, color.g, color.b);
    }
    geometry.setAttribute('position', new THREE.Float32BufferAttribute(positions, 3));
    geometry.setAttribute('color', new THREE.Float32BufferAttribute(colors, 3));
    const material = new THREE.PointsMaterial({ size: 0.15, vertexColors: true });
    const stars = new THREE.Points(geometry, material);
    scene.add(stars);

    // Animation loop for galaxy
    function animate() {
        requestAnimationFrame(animate);
        stars.rotation.y += 0.0008;
        stars.rotation.x += 0.0002;
        renderer.render(scene, camera);
    }
    animate();
});
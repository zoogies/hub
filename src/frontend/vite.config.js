import { sveltekit } from '@sveltejs/kit/vite';

const config = {
	plugins: [sveltekit()],
	server: {
		proxy: {
			'/api': {
				 target: 'https://127.0.0.1:5000',
				 changeOrigin: true,
				 secure: false,      
				 ws: true,
		  }
		}
	}
};

export default config;
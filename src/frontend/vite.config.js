import { sveltekit } from '@sveltejs/kit/vite';

const config = {
	plugins: [sveltekit()],
	server: {
		proxy: {
			'/api': {
				 target: 'https://zoogies.live',
				 changeOrigin: true,
				 secure: false,      
				 ws: true,
		  }
		}
	}
};

export default config;
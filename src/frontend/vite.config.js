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
		},
	},
	define: {
		__VERSION__: JSON.stringify(process.env.npm_package_version),
	}
};

export default config;
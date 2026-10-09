import { defineConfig } from 'vite';
import { resolve } from 'path';

export default defineConfig({
  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        products: resolve(__dirname, 'products.html'),
        services: resolve(__dirname, 'services.html'),
        projects: resolve(__dirname, 'projects.html'),
        signature: resolve(__dirname, 'signature.html'),
        why: resolve(__dirname, 'why-nsp.html'),
        collaboration: resolve(__dirname, 'collaboration.html'),
        contact: resolve(__dirname, 'contact.html'),
      },
    },
  },
});

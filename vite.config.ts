import EslintPlugin from 'vite-plugin-eslint';
import StyleLintPlugin from 'vite-plugin-stylelint';
import AutoImport from 'unplugin-auto-import/vite';
import Components from 'unplugin-vue-components/vite';
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers';

import { defineConfig, loadEnv } from 'vite';
import path from 'path';

import { createSvgIconsPlugin } from 'vite-plugin-svg-icons';
import vue from '@vitejs/plugin-vue';
import { fileURLToPath, URL } from 'node:url';
import VitePluginFonts from 'vite-plugin-fonts';

const styleLintConfig = StyleLintPlugin({
  files: ['src/**/*.{vue,scss}'],
  fix: true,
});

const eslintConfig = EslintPlugin({
  fix: true,
  cache: false,
});

// TODO: Убрать. Пример подключения шрифтов
const fontsConfig = VitePluginFonts({
  custom: {
    families: [
      {
        name: 'Roboto',
        local: 'Roboto',
        src: './src/assets/fonts/*.ttf',
      },
    ],
  },
});

const autoImportConfig = AutoImport({
  resolvers: [ElementPlusResolver()],
});

const componentsConfig = Components({
  resolvers: [ElementPlusResolver()],
});

const svgIconsConfig = createSvgIconsPlugin({
  iconDirs: [path.resolve(process.cwd(), 'src/assets/icons')],
  symbolId: 'icon-[dir]-[name]',
  inject: 'body-first',
  customDomId: '__svg__icons__dom__',
});

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '') as ImportMetaEnv;

  return {
    server: {
      proxy: {
        '/api': {
          target: env.VITE_BASE_URL,
          changeOrigin: true,
          secure: false,
        },
      },
    },
    test: {
      globals: true,
      environment: 'jsdom',
    },
    plugins: [vue(), styleLintConfig, eslintConfig, autoImportConfig, componentsConfig, svgIconsConfig, fontsConfig],
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "@/styles/resources" as *; @use "@/styles/vendor" as *;',
        },
      },
    },
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url)),
      },
    },
  };
});

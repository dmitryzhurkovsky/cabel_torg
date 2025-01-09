// https://v3.nuxtjs.org/api/configuration/nuxt.config


export default defineNuxtConfig({
  runtimeConfig: {
    public:{
      NUXT_APP_API_URL: process.env.NUXT_APP_API_URL,
      NUXT_APP_IMAGES: process.env.NUXT_APP_IMAGES,
      NUXT_APP_DOCUMENTS: process.env.NUXT_APP_DOCUMENTS
    }
  },
  vite: {
    css: {
      preprocessorOptions: {
        scss: {
          additionalData: '@use "@/assets/styles/main.scss" as *;'
        }
      }
    }
  },
  build: {
    transpile: ['swiper'],
  },
  modules: [
    [
      'yandex-metrika-module-nuxt3',
      {
        id: '94113822',
        webvisor: true,
        // clickmap: true,
        // useCDN: false,
        // trackLinks: true,
        // accurateTrackBounce: true,
      }
    ]
  ],

  // pages: true

  ssr: true,
});



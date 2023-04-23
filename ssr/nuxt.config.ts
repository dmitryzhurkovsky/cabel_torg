// https://v3.nuxtjs.org/api/configuration/nuxt.config


export default defineNuxtConfig({
  runtimeConfig: {
    public:{
      NUXT_APP_API_URL: process.env.NUXT_APP_API_URL,
      NUXT_APP_IMAGES: process.env.NUXT_APP_IMAGES
    }
  },
});

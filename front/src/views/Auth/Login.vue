<template>
  <div id="Login" class="login">
       <h2>Вход</h2>
      <div class="container_login">
        <form class="login_form">
            <input
              type="email"
              class="form-control"
              :class="{ 'is-invalid': errors.email }"
              id="email"
              v-model="details.email"
              placeholder="Email"
            />
            <div class="invalid-feedback" v-if="errors.email">
              {{ errors.email[0] }}
            </div>
            <input
              type="password"
              class="form-control"
              :class="{ 'is-invalid': errors.password }"
              id="password"
              v-model="details.password"
              placeholder="Password"
            />
            <div class="invalid-feedback" v-if="errors.password">
              {{ errors.password[0] }}
            </div>
          <button type="button" @click="login">
            Войти
          </button>
        </form>
     </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Login",

  data: function() {
    return {
      details: {
        email: null,
        password: null
      }
    };
  },

  computed: {
    ...mapGetters(["errors"]),
    ...mapGetters("auth", ["user"]),

  },

  mounted() {
    this.$store.commit("setErrors", {});
  },

  methods: {
    ...mapActions("auth", ["sendLoginRequest"]),

    login: function() {
      this.sendLoginRequest(this.details).then(() => {
        this.$router.push({ name: "Home" });
      });
    },
  }
};
</script>

<style lang="scss">
</style>

<template>
  <div class="registration">
      <h2> Регистрация</h2>

      <div class="container">
        <form>
          <div class="form-group">
            <input
              type="email"
              class="form-control"
              :class="{ 'is-invalid': errors.email }"
              id="email"
              v-model="details.email"
              placeholder="Enter email"
            />
            <div class="invalid-feedback" v-if="errors.email">
              {{ errors.email[0] }}
            </div>
          </div>
          <div class="form-group">
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
          </div>
          <div class="form-group">
            <input
              type="password"
              class="form-control"
              id="password_confirmation"
              v-model="details.password_confirmation"
              placeholder="Confirm password"
            />
          </div>
          <button type="button" @click="register" class="">Регистрация</button>
        </form>
      </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Register",

  data: function() {
    return {
      details: {
        name      : null,
        email     : null,
        password  : null,
        password_confirmation: null,
      }
    };
  },

  computed: {
    ...mapGetters(["errors"]),
  },

  async mounted() {

    this.$store.commit("notification/ADD_MESSAGE", []);
  },

  methods: {
    ...mapActions("auth", ["sendRegisterRequest"]),

    register: function() {
      if (this.details.name){
        this.sendRegisterRequest(this.details).then(() => {
           this.$router.push({ name: "Home" });
        });
      } else {
        // this.$store.commit('view/ADD_MESSAGE', {name: 'Не указан Ник или клуб!', icon: 'error', id: '1'})
      }
    },
  },

};
</script>

<style lang="scss">



</style>

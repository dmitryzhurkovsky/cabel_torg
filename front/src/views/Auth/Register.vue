<template>
  <div class="registration">
      <h2> Регистрация</h2>

      <div class="container">
        <form>
          <div class="form-group">
            <input
              type="email"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.email }"
              id="email"
              v-model="details.email"
              placeholder="Enter email"
            />
            <div class="invalid-feedback" v-if="ERRORS.email">
              {{ errors.email[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.full_name }"
              id="full_name"
              v-model="details.full_name"
              placeholder="Enter full_name"
            />
            <div class="invalid-feedback" v-if="ERRORS.full_name">
              {{ errors.full_name[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="phone"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.phone_number }"
              id="phone_number"
              v-model="details.phone_number"
              placeholder="Enter phone_number"
            />
            <div class="invalid-feedback" v-if="ERRORS.phone_number">
              {{ errors.phone_number[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.company_name }"
              id="company_name"
              v-model="details.company_name"
              placeholder="Enter company_name"
            />
            <div class="invalid-feedback" v-if="ERRORS.company_name">
              {{ errors.company_name[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="number"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.unp }"
              id="unp"
              v-model="details.unp"
              placeholder="Enter unp"
            />
            <div class="invalid-feedback" v-if="ERRORS.unp">
              {{ errors.unp[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.legal_address }"
              id="legal_address"
              v-model="details.legal_address"
              placeholder="Enter legal_address"
            />
            <div class="invalid-feedback" v-if="ERRORS.legal_address">
              {{ errors.legal_address[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.IBAN }"
              id="IBAN"
              v-model="details.IBAN"
              placeholder="Enter IBAN"
            />
            <div class="invalid-feedback" v-if="ERRORS.IBAN">
              {{ errors.IBAN[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.BIC }"
              id="BIC"
              v-model="details.BIC"
              placeholder="Enter BIC"
            />
            <div class="invalid-feedback" v-if="ERRORS.BIC">
              {{ errors.BIC[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="text"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.serving_bank }"
              id="serving_bank"
              v-model="details.serving_bank"
              placeholder="Enter serving_bank"
            />
            <div class="invalid-feedback" v-if="ERRORS.serving_bank">
              {{ errors.serving_bank[0] }}
            </div>
          </div>
          <div class="form-group">
            <input
              type="password"
              class="form-control"
              :class="{ 'is-invalid': ERRORS.password }"
              id="password"
              v-model="details.password"
              placeholder="Password"
            />
            <div class="invalid-feedback" v-if="ERRORS.password">
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
        id        : null,
        email     : null,
        full_name : null,
        phone_number: null,
        company_name: null,
        unp       : null,
        legal_address: null,
        IBAN      : null,
        BIC       : null,
        serving_bank: null,
        password  : null,
        password_confirmation: null,
      }
    };
  },

  computed: {
    ...mapGetters("auth",["ERRORS"]),
  },

  async mounted() {
    // this.$store.commit("notification/ADD_MESSAGE", []);
  },

  methods: {
    ...mapActions("auth", ["SEND_REGISTER_REQUEST"]),

    register: function() {
      // if (this.details.name){
        this.SEND_REGISTER_REQUEST(this.details).then(() => {
           this.$router.push({ name: "Main" });
        });
      // } else {
      //   this.$store.commit('view/ADD_MESSAGE', {name: 'Не указан Ник или клуб!', icon: 'error', id: '1'})
      // }
    },
  },

};
</script>

<style lang="scss">



</style>

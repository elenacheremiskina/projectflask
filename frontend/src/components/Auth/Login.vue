<template>
  <div class="content-wrapper">
    <section>
      <div class="container">
        <div class="auth">
          <div class="auth__form">
            <div>
              <b-card title="Вход">
                <b-form-group label="Электронная почта:">
                  <b-form-input
                    type="email"
                    placeholder="Введите электронную почту"
                    v-model="email"
                    class="email-input"
                  />
                </b-form-group>
                <b-form-group label="Пароль:">
                  <b-form-input
                    type="password"
                    placeholder="Введите пароль"
                    v-model="password_hash"
                    class="password_hash-input"
                  />
                </b-form-group>
                <b-button
                  type="button auth-button"
                  class="btn btn-dark"
                  @click="handleSubmit"
                  >Войти</b-button
                >
                <div class="buttons-list buttons-list--info">
                  <span>
                    Нужна регистрация?
                    <router-link to="/registration">Нажмите сюда</router-link>
                  </span>
                </div>
              </b-card>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Axios from "axios";
import { mapState } from "vuex";
export default {
  computed: {
    ...mapState({
      userStore: (state) => state.userStore,
    }),
  },
  data: function() {
    return {
      email: "",
      password_hash: "",
      isHidden: false,
    };
  },
  methods: {
    handleSubmit: function(e) {
      e.preventDefault();
      window.localStorage.removeItem('authUser')
      window.localStorage.removeItem('id_text')
      const authUser = {};
      const url = "http://localhost:5000/api/login";
      if (this.email && this.password_hash) {
        Axios.post(url, {
          email: this.email,
          password_hash: this.password_hash,
        })
          .then((res) => {
            //
            if (res.status === 200) {
              console.log("Oauth token", res);
              authUser.access_token = res.data.access_token;
              authUser.refresh_token = res.data.refresh_token;
              window.localStorage.setItem("authUser", JSON.stringify(authUser));
              this.$store.dispatch("setUserObject", authUser);
              if (localStorage.getItem("authUser") !== null) {
                this.$router.push("dashboard");
              }
            }
          })
          .catch(function(err) {
            console.error(err);
          });
      }
    },
  },
};
</script>

<style scoped>
.auth {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

.auth__banner,
.auth__form {
  width: 50%;
}

@media screen and (max-width: 768px) {
  .auth__banner,
  .auth__form {
    width: 100%;
    margin-bottom: 30px;
  }

  .auth__banner:last-child,
  .auth__form:last-child {
    margin-bottom: 0;
  }
}

.auth__form {
  max-width: 400px;
}

.form-item .error {
  display: none;
  margin-bottom: 8px;
  font-size: 13.4px;
  color: #fc5c65;
}

.form-item.errorInput .error {
  display: block;
}

input.error {
  border-color: #fc5c65;
  animation: shake 0.3s;
}

.buttons-list {
  text-align: right;
  margin-bottom: 20px;
}

.buttons-list.buttons-list--info {
  text-align: center;
}

.buttons-list.buttons-list--info:last-child {
  margin-bottom: 0;
}

a {
  color: #444ce0;
}
</style>

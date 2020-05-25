<template>
  <div class="content-wrapper">
    <section>
      <div class="container">
        <div class="auth">
          <div class="auth__form">
            <div>
              <b-card title="Регистрация" style="margin:0 auto">
                <b-form-group label="Электронная почта:">
                  <b-form-input
                    type="email"
                    placeholder="Введите электронную почту"
                    v-model="email"
                    class="email-input"
                    id="email"
                  />
                </b-form-group>
                <b-form-group label="Фамилия:">
                  <b-form-input
                    type="text"
                    placeholder="Введите фамилию"
                    v-model="surname"
                    class="input"
                    id="surname"
                  />
                </b-form-group>
                <b-form-group label="Имя:">
                  <b-form-input
                    type="text"
                    placeholder="Введите имя"
                    v-model="name"
                    class="input"
                    id="name"
                  />
                </b-form-group>
                <b-form-group label="Отчество:">
                  <b-form-input
                    type="text"
                    placeholder="Введите отчество"
                    v-model="patronymic"
                    class="input"
                    id="patronymic"
                  />
                </b-form-group>
                <b-form-group label="Должность:">
                  <b-form-input
                    type="text"
                    placeholder="Введите должность"
                    v-model="position"
                    class="input"
                    id="position"
                  />
                </b-form-group>
                <b-form-group label="Пароль:">
                  <b-form-input
                    type="password"
                    placeholder="Введите пароль"
                    v-model="password_hash"
                    class="password_hash-input"
                    id="password_hash"
                  />
                </b-form-group>
                <b-button
                  type="button auth-button"
                  class="btn btn-dark"
                  v-on:click="handleSubmit"
                >Зарегистрироваться</b-button>
                <div class="buttons-list buttons-list--info">
                  <span>
                    Уже есть аккаунт?
                    <router-link to="/">Нажмите сюда</router-link>
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
      userStore: state => state.userStore
    })
  },
  props: ["nextUrl"],
  data: function() {
    return {
      email: "",
      surname: "",
      name: "",
      patronymic: "",
      position: "",
      password_hash: "",
      isHidden: false
    };
  },
  methods: {
    handleSubmit: function(e) {
      e.preventDefault();
      const url = "http://localhost:5000/api/register";
      if (
        this.email &&
        this.surname &&
        this.name &&
        this.patronymic &&
        this.position &&
        this.password_hash
      ) {
        Axios.post(url, {
          email: this.email,
          surname: this.surname,
          name: this.name,
          patronymic: this.patronymic,
          position: this.position,
          password_hash: this.password_hash
        })
          .then(res => {
            console.log(res);
            localStorage.setItem("authUser", res.data.access_token);
            if (localStorage.getItem("authUser") != null) {
              this.$emit("loggedIn");
              this.$router.push("/");
            }
          })
          .catch(function(err) {
            console.error(err);
          });
      }
    }
  }
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

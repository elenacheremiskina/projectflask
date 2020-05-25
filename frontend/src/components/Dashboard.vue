 <template>
  <div class="p-grid p-fluid dashboard">
    <div class="p-col-12">
      <div>
        <b-card title="Загрузка файла">
          <div class="form-group">
            <form id="upload_form" role="form" enctype="multipart/form-data">
              <input type="file" class="inputfile" name="file" id="file" accept=".txt" />
              <input type="button" style="float:right;" @click="upload" value="Отправить" />
            </form>
          </div>
        </b-card>
      </div>
    </div>
    <!-- <div class="p-col-12">
      <div>
        <b-card title="Редактор">
          <Editor editorStyle="height: 320px"/>
        </b-card>
      </div>
    </div>-->
  </div>
</template>

<script>
import Axios from "axios";
export default {
  data() {
    return {
      file: null,
      text: "",
      type: ""
      // file: ""
    };
  },
  created() {
    try {
      document.getElementById("toggler").style.visibility = "visible";
      document.getElementById("switch").style.visibility = "visible";
    } catch {
      null;
    }
  },
  methods: {
    upload: function(e) {
      e.preventDefault();
      var data = new FormData();
      data.append("file", document.getElementById("file").files[0]);
      console.log(document.getElementById("file").files[0]);
      const authUser = JSON.parse(window.localStorage.getItem("authUser"));
      const token = authUser.access_token;
      Axios.post("http://localhost:5000/api/text", data, {
        headers: {
          Authorization: `Bearer ${token}`,
          "Content-Type": "application/json"
        }
      })
        .then(response => {
          console.log(response);
          this.$router.push("sample");
        })
        .catch(function(err) {
          console.error(err);
        });
    }
  },
  mounted: function() {
    this.$nextTick(function() {
      try {
        document.getElementById("toggler").style.visibility = "visible";
        document.getElementById("switch").style.visibility = "visible";
      } catch {
        null;
      }
    });
  }
};
</script>

<style scoped>
</style>

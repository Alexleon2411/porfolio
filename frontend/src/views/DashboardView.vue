<template>
  <v-container>

    <div>
      <section>
        <h1>Add new note</h1>
        <hr/><br/>

        <form @submit.prevent="submit">
          <div class="mb-3">
            <label for="title" class="form-label">Title:</label>
            <input type="text" name="title" v-model="form.title" class="form-control" />
          </div>
          <div class="mb-3">
            <label for="content" class="form-label">Content:</label>
            <textarea
              name="content"
              v-model="form.content"
              class="form-control"
            ></textarea>
          </div>
          <div class="mb-3">
            <label for="image" class="form-label">Image:</label>
            <input type="file" id="image" name="image" v-on:change="onFileChange" class="form-control-file">
            <img  class="preview-image">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </section>

      <br/><br/>

      <section>
        <h1>Notes</h1>
        <hr/><br/>

        <div v-if="skills.length">
          <div v-for="skill in skilss" :key="skill.id" class="notes">
            <div class="card" style="width: 18rem;">
              <div class="card-body">
                <ul>
                  <li><strong>Skill Title:</strong> {{ skill.title }}</li>
                  <li><strong>Author:</strong> {{ skill.author.username }}</li>
                  <li><router-link :to="{name: 'Skill', params:{id: skill.id}}">View</router-link></li>
                </ul>
              </div>
            </div>
            <br/>
          </div>
        </div>

        <div v-else>
          <p>Nothing to see. Check back later.</p>
        </div>
      </section>
    </div>
  </v-container>
</template>

<script>
import { defineComponent } from 'vue';
import { mapGetters, mapActions } from 'vuex';

export default defineComponent({
  name: 'Dashboard',
  data() {
    return {
      form: {
        title: '',
        content: '',
        image: '',
      },
    };
  },
  created: function() {
    return this.$store.dispatch('getSkills');
  },
  computed: {
    ...mapGetters({ skills: 'stateSkills'}),
  },
  methods: {
    ...mapActions(['createSkill']),
    async submit() {
      await this.createSkill(this.form);
    },
  },
});
</script>

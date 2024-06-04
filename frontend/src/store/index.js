import { createStore } from "vuex";

import skills from './modules/skills';
import projects from './modules/projects';
import users from './modules/users';

export default createStore({
  modules: {
    skills,
    projects,
    users,
  }
});

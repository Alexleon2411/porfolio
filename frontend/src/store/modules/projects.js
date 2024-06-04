import axios from 'axios';

const state = {
  projects: null,
  project: null
};

const getters = {
  stateProjects: state => state.projects,
  stateProject: state => state.project,
};

const actions = {
  async createProject({dispatch}, project) {
    await axios.post('projects', project);
    await dispatch('getProjects');
  },
  async getProjects({commit}) {
    let {data} = await axios.get('projects');
    commit('setProjects', data);
  },
  async viewProject({commit}, id) {
    let {data} = await axios.get(`project/${id}`);
    commit('setProject', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateProject({}, project) {
    await axios.patch(`project/${project.id}`, project.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteProject({}, id) {
    await axios.delete(`project/${id}`);
  }
};

const mutations = {
  setProjects(state, projects){
    state.projects = projects;
  },
  setProject(state, project){
    state.project = project;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};

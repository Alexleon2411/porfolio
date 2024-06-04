import axios from 'axios';

const state = {
  skills: null,
  skill: null
};

const getters = {
  stateSkills: state => state.skills,
  stateSkill: state => state.skill,
};

const actions = {
  async createSkill({dispatch}, skill) {
    await axios.post('skills', skill);
    await dispatch('getSkills');
  },
  async getSkills({commit}) {
    let {data} = await axios.get('skills');
    commit('setSkills', data);
  },
  async viewSkill({commit}, id) {
    let {data} = await axios.get(`skill/${id}`);
    commit('setSkill', data);
  },
  // eslint-disable-next-line no-empty-pattern
  async updateSkill({}, skill) {
    await axios.patch(`skill/${skill.id}`, skill.form);
  },
  // eslint-disable-next-line no-empty-pattern
  async deleteSkill({}, id) {
    await axios.delete(`skill/${id}`);
  }
};

const mutations = {
  setSkills(state, skills){
    state.skills = skills;
  },
  setSkill(state, skill){
    state.skill = skill;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};

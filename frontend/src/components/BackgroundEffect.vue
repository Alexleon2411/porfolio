<template>
  <div class="container">
    <div class="image-container" ref="imageContainer">
      <div
        v-for="(piece, index) in pieces"
        :key="index"
        :ref="`piece-${index}`"
        :class="`piece piece-${index}`"
      ></div>
    </div>
    <div class="replacement-image"></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pieces: Array.from({ length: 50 }), // Ajusta el número de pedazos según sea necesario
    };
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll);
  },
  beforeDestroy() {
    //window.removeEventListener('scroll', this.handleScroll);
  },
  methods: {
    handleScroll() {
      const container = this.$refs.imageContainer;
      const scrollPosition = window.scrollY;
      const containerHeight = container.offsetHeight;
      const windowHeight = window.innerHeight;
      const scrollRatio = Math.min(scrollPosition / (containerHeight - windowHeight), 1);

      this.pieces.forEach((_, index) => {
        const piece = this.$refs[`piece-${index}`][0];
        if (piece) {
          const fallDistance = scrollRatio * 900; // Ajusta la distancia de caída según sea necesario
          piece.style.transform = `translateY(${fallDistance}px)`;
          piece.style.opacity = 1 - scrollRatio;
        }
      });
    },
  },
};
</script>

<style lang="scss">


.image-container {
  position: relative;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  background-image: url(../imgs/header.jpg);
  background-size: cover;
  background-position: center;
  display: flex;
  flex-wrap: wrap;
}

.piece {
  width: 10%; // Ajusta el tamaño de los pedazos según sea necesario
  height: 10%;
  background-image: url(../imgs/header.jpg);
  background-size: cover;
  background-position: center;
  position: absolute;
  transition: transform 0.3s ease, opacity 0.3s ease;

  &.piece-0  { background-position: 0% 5%; }
  &.piece-1  { background-position: 10% 15%; }
  &.piece-2  { background-position: 20% 30%; }
  &.piece-3  { background-position: 40% 45%; }
  &.piece-4  { background-position: 50% 60%; }
  // Agrega más posiciones según sea necesario
}

.replacement-image {
  height: 100vh;
  background-image: url(../imgs/pexels-pixabay-33109.jpg);
  background-size: cover;
  background-position: center;
}
</style>

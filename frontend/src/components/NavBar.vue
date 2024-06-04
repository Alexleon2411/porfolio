<template>
  <nav class="custom-navbar" data-spy="affix" data-offset-top="20">
    <div class="container">
      <a class="logo" href="#">Alejandro</a>
      <ul class="nav">
        <li class="item">
          <a class="link" href="#home">Home</a>
        </li>
        <li class="item">
          <a class="link" href="#about">About</a>
        </li>
        <li class="item">
          <a class="link" href="#portfolio">Portfolio</a>
        </li>
        <li class="item">
          <a class="link" href="#contact">Contact</a>
        </li>
      </ul>
      <a href="javascript:void(0)" id="nav-toggle" class="hamburger hamburger--elastic">
        <div class="hamburger-box">
          <div class="hamburger-inner"></div>
        </div>
      </a>
    </div>
  </nav>
</template>
<script>
import $ from 'jquery'

export default {
  name: 'Navbar',
  mounted() {
    $(document).ready(function() {
      $(".custom-navbar .link").on('click', function(event) {
        if (this.hash !== "") {
          event.preventDefault();
          var hash = this.hash;
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 700, function() {
            window.location.hash = hash;
          });
        }
      });

      // navbar toggle
      $('#nav-toggle').click(function() {
        $(this).toggleClass('is-active');
        $('ul.nav').toggleClass('show');
      });
    });
  }
}
</script>

<!--  -->

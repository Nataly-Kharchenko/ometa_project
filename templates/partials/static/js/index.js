webpackJsonp([0],[
/* 0 */,
/* 1 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


/**
 * App entry point.
 *
 * @module App
 */

/** Import initialized-by-default modules/libs */

__webpack_require__(2);

/***/ }),
/* 2 */
/***/ (function(module, exports, __webpack_require__) {

"use strict";


Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

/**
 * Website's common scripts.
 *
 * @module Common
 */

var Common = exports.Common = function () {
  /**
   * Cache data, make preparations and initialize common scripts.
   */
  function Common() {
    _classCallCheck(this, Common);

    // cache data, make preparations etc.
    this.$nav = $('.nav');
    this.$burger = $('.burger');
    this.$backdrop = $('.backdrop');
    this.jsMatrix = document.querySelectorAll('.js-matrix');

    this.artistsBlock = $('.js-artists');
    this.$mainIframeVideo = $('.js-rnd-video');

    // initialize after construction
    this.init();

    // window.addEventListener('resize', () => {
    //   this.matrixStyleRounding(this.jsMatrix);
    // });
  }

  /**
   * Example method.
   */


  _createClass(Common, [{
    key: 'navigation',
    value: function navigation() {
      var _this = this;

      if (window.innerWidth > 450) {
        this.$burger.hover(function (_) {
          return _this.$burger.addClass('open');
        }, function (_) {
          return _this.$burger.removeClass('open');
        });
        this.$nav.hover(function (_) {
          return _this.$burger.addClass('open');
        }, function (_) {
          return _this.$burger.removeClass('open');
        });
      } else {
        this.$burger.click(function (_) {
          if (_this.$burger.hasClass('open')) {
            _this.$burger.removeClass('open');
            _this.$backdrop.removeClass('active');
          } else {
            _this.$burger.addClass('open');
            _this.$backdrop.addClass('active');
          }
        });
      }
    }
  }, {
    key: 'artistsBlockInit',
    value: function artistsBlockInit() {
      if (this.artistsBlock) {
        var artistsPreview = this.artistsBlock.find('.js-artists-preview');
        var artistsNamesList = this.artistsBlock.find('.js-artists-names');

        artistsNamesList.hover(function () {
          var $self = $(this);
          var dataNum = $self.data('num');
          artistsNamesList.removeClass('active');
          $self.addClass('active');

          artistsPreview.removeClass('active');
          artistsPreview.eq('active');

          artistsPreview.filter(function () {
            return $(this).data('num') == dataNum;
          }).addClass('active');
        });
      }
    }
  }, {
    key: 'initPreviewSlider',
    value: function initPreviewSlider() {
      var slideWidth = 620;
      var nextVisibleWidth = 80;
      var spaceBetween = (window.innerWidth - slideWidth) / 2;
      var $previewSlider = $('.js-preview-slider');
      var $foldersSliders = $('.js-folder-slider');
      var $allFoldersWrap = $('.js-all-folders-wrap');
      var $allSlides = void 0;

      if ($previewSlider.length) {
        new Swiper('.js-preview-slider', {
          direction: 'horizontal',
          slidesPerView: 2,
          spaceBetween: spaceBetween,
          speed: 700,
          centeredSlides: true,
          slideToClickedSlide: true,

          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          },
          on: {
            init: function init() {
              $allSlides = $previewSlider.find('.swiper-slide');
              $allSlides.eq(this.activeIndex).addClass('o-active');
            },
            click: function click() {
              var _this2 = this;

              var clickedIndex = this.clickedIndex + 1;

              if (clickedIndex > 0) {
                $allSlides.removeClass('o-active');
                setTimeout(function () {
                  _this2.clickedSlide.classList.add('o-active');
                }, 200);
              }

              // let clickedIndex = this.clickedIndex + 1;
              // if (clickedIndex > 0 && this.clickedSlide.classList.contains('swiper-slide-active')) {
              //   $allFoldersWrap.addClass('active');
              //   $foldersSliders
              //     .removeClass('active')
              //     .filter(function () {
              //       return $(this).data('num') == clickedIndex;
              //     }).addClass('active');
              // }
            },
            slideChange: function slideChange() {
              $allSlides.removeClass('o-active');
              var activeIndex = this.activeIndex;

              setTimeout(function () {
                $allSlides.eq(activeIndex).addClass('o-active');
              }, 200);
            }
          },

          breakpoints: {
            // when window width is <= 450
            450: {
              slidesPerView: 1,
              spaceBetween: 20
            }
          }
        });

        $('.preview-slider__media').click(function () {
          var $self = $(this);
          var clickedIndex = parseInt($self.data('num'));
          var $slide = $self.closest('.swiper-slide');

          if (clickedIndex > 0 && $slide.hasClass('o-active')) {
            $allFoldersWrap.addClass('active');

            $foldersSliders.removeClass('active').filter(function () {
              return $(this).data('num') == clickedIndex;
            }).addClass('active');
          }
        });

        $foldersSliders.each(function (i, el) {
          initSlider(el);
        });

        $('.js-close-folder').click(function () {
          $allFoldersWrap.removeClass('active');
          $foldersSliders.removeClass('active');
        });
      }

      function initSlider(selectorOrHtmlEl) {
        new Swiper(selectorOrHtmlEl, {
          direction: 'horizontal',
          slidesPerView: 1,
          spaceBetween: 20,
          speed: 700,
          centeredSlides: true,
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
        });
      }
    }
  }, {
    key: 'initVimeoVideos',
    value: function initVimeoVideos() {
      // $('.js-vimeo-video').

      // $('.js-vimeo-video').mouseover(function() {
      //   var player = $("#" + this.id);
      //   var froogaloop = $f(player[0].id);
      //
      //   froogaloop.addEvent('ready', function(e) {
      //     e.preventDefault();
      //     console.log('$f = ', froogaloop);
      //
      //     froogaloop.api('play');
      //     player.mouseout(function () {
      //       froogaloop.api('pause');
      //     });
      //   }
      // });
    }
  }, {
    key: 'randomVideoInit',
    value: function randomVideoInit() {
      var vimeoVideosIds = ['wild-dance.mp4', 'bit-beach.mp4', 'kryla.mp4', 'always beautiful.mp4'];

      var rndVimoeId = vimeoVideosIds[Math.floor(Math.random() * vimeoVideosIds.length)];
      // var fullPathToVideo = 'https://player.vimeo.com/video/' + rndVimoeId + '?background=1&autoplay=1&loop=1&byline=0&title=0&controls=0';
      // var fullPathToVideo = 'https://player.vimeo.com/video/' + rndVimoeId + '?background=1&autoplay=1&loop=1&byline=0&title=0&controls=0';
      var fullPathToVideo = 'static/video/' + rndVimoeId;

      this.$mainIframeVideo.attr('src', fullPathToVideo);

      console.log('fullPathToVideo', fullPathToVideo);

      // var iframe = document.querySelector('#js-rnd-video');
      // var player = new Vimeo.Player(iframe);

      // player.on('play', function() {
      //   console.log('Played the video');
      // });
      //
      // player.play();
      // player.disableTextTrack();
      // player.setVolume(0);
      //
      // Promise.all([player.getVideoWidth(), player.getVideoHeight()]).then((dimensions) => {
      //   var width = dimensions[0];
      //   var height = dimensions[1];
      //
      //   this.$mainIframeVideo.css('height', (height / width * 100).toFixed(2) + 'vw');
      //   this.$mainIframeVideo.css('min-width', (width / height * 100).toFixed(2) + 'vh');
      // });
    }

    // recalc matrix (округление значений к integer)

  }, {
    key: 'matrixStyleRounding',
    value: function matrixStyleRounding(inObj) {
      if (inObj) {
        for (var i = 0; i < inObj.length; ++i) {
          var tmpObj = inObj[i];
          tmpObj.style.transform = '';
          var matrix = getComputedStyle(tmpObj).transform;
          matrix = matrix.slice(7, -1).split(' ').map(function (item) {
            return parseInt(item);
          });
          tmpObj.style.transform = 'matrix(' + matrix.join(',') + ')';
        }
      }
    }

    /**
     * Initialize common scripts.
     */

  }, {
    key: 'init',
    value: function init() {
      // this.randomVideoInit();
      this.navigation();
      this.artistsBlockInit();
      this.initPreviewSlider();
      this.initVimeoVideos();
    }
  }]);

  return Common;
}();

/** Export initialized common scripts by default */


exports.default = new Common();

/***/ })
],[1]);
//# sourceMappingURL=index.js.map
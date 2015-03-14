module.exports = function(grunt) {
  var jsDevFiles = ['snabbafakta/static/js/app.js'],
      cssDevFiles = ['snabbafakta/static/css/style.scss'];

  grunt.initConfig({
    concat: {
      scripts: {
        src: jsDevFiles,
        dest: 'snabbafakta/static/js/combined.js'
      }
    },
    uglify: {
      build: {
        src: 'snabbafakta/static/js/combined.js',
        dest: 'snabbafakta/static/js/combined_min.js'
      }
    },
    sass: {
      dist: {
        options: {
          style: 'compressed'
        },
        files: {
          'snabbafakta/static/css/style_built.css': 'snabbafakta/static/css/style.scss'
        }
      }
    },
    autoprefixer: {
      options: {
        browsers: ['last 2 versions', 'ie 8', 'ie 9']
      },
      build: {
        src: 'snabbafakta/static/css/style_built.css',
        dest: 'snabbafakta/static/css/style.css'
      }
    },
    watch: {
      scripts: {
        files: jsDevFiles,
        tasks: ['concat:scripts', 'uglify']
      },
      styles: {
        files: cssDevFiles,
        tasks: ['sass', 'autoprefixer']
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-autoprefixer');

  grunt.registerTask('default', [
    'sass',
    'concat',
    'autoprefixer',
    'uglify'
  ]);
  grunt.registerTask('dev', ['default', 'watch']);
};

module.exports = function(grunt) {
  grunt.initConfig({
    concat: {
      scripts: {
        src: [
          'static/js/*.js'
        ],
        dest: 'static/js/combined.js'
      }
    },
    uglify: {
      build: {
        src: 'static/js/combined.js',
        dest: 'static/js/combined_min.js'
      }
    },
    watch: {
      scripts: {
        files: ['static/js/*.js'],
        tasks: ['concat:scripts', 'uglify']
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', [
    'concat',
    'uglify'
  ]);
  grunt.registerTask('dev', ['default', 'watch']);
};

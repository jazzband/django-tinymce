/**
 * User: andriy
 * Date: 02/04/13
 * Time: 22:47
 * Class for
 */
(function (dir) {
    if ( window.filebrowserPath ) {
        return;
    }
    window.filebrowserPath = {
        getDefaultPath: function () {
            return dir;
        }
    }
})("{{ dir }}");
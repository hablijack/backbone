var Frontend = (function() {

    var initClock = function() {
        Frontend.updateClock()
        setInterval('Frontend.updateClock()', 60000);
    };

    return {
        init: function() {
            initClock();
        },

        updateClock: function() {
            $('.clock').html(moment().locale('de').format('LLL'));
        }
    };
})();

$(document).ready( function() {
	Frontend.init();
});

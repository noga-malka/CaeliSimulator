if (!window.dash_clientside) {
    window.dash_clientside = {};
}
window.dash_clientside.clientside = {
    make_draggable: function(id) {
        setTimeout(function() {
            var el = document.getElementById(id)
            window.console.log(el)
            dragula([el], {direction:'squared'})
        }, 1)
        return window.dash_clientside.no_update
    }
}
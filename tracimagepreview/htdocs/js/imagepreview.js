jQuery(document).ready(function ($) {
    (function() {
        offset = {
            x: 10,
            y: 10
        };

        $('#attachments dt > a:first-child, #changelog table[class="changes"] a:first-child').hover(function(e) {
            if (!this.text.match(/(\.png|\.jpe?g|\.gif|\.bmp)/g)) {
                return;
            }
            this.t = this.title;
            this.title = "";
            var desc = $(this.parentNode.nextElementSibling);
            var caption = ((desc.prop('tagName') == 'DD') ? '<br />' + desc.text() : (this.t != "") ? '<br />' + this.t : '');
            var url = this.href.replace(/attachment/g, 'raw-attachment');
            $('body').append('<p id="image-preview"><img src="' + url + '" alt="Image preview" style="max-width: 300px"/>' + caption + '</p>');
            $('#image-preview')
                .css('top', (e.pageY + offset.y) + 'px')
                .css('left', (e.pageX + offset.x) + 'px')
                .fadeIn('fast');
        }, function() {
            if (this.t != null) {
                this.title = this.t;
            }
            $('#image-preview').remove();
        });
        $('#attachments dt > a:first-child, #changelog table[class="changes"] a:first-child').mousemove(function(e) {
            $('#image-preview')
                .css('top', (e.pageY + offset.y) + 'px')
                .css('left', (e.pageX + offset.x) + 'px');
        });
    })();
});

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function sendFile(file, editor, welEditable) {
            data = new FormData();
            data.append("file", file);
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                data: data,
                type: "POST",
                url: "/ideia-summernote/upload",
                cache: false,
                contentType: false,
                processData: false,
                success: function(data) {
                    editor.insertImage(welEditable, data.url);
                }
                ,
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });
    return false;
}
$(function init() {
  var $editor = $(document).find('[data-toggle="editor"]');
  var editorConfig = $editor.data('config') || {};


  console.dir(editorConfig);
  $editor.summernote({
      callbacks: {
          onImageUpload: function(files, editor, welEditable) {
              console.log(arguments);
          // upload image to server and create imgNode...
            sendFile(files[0],editor,welEditable);
          //$editor.summernote('insertNode', imgNode);
        }
      }
  });
});

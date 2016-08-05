$(function init() {
  var $editor = $(document).find('[data-toggle="editor"]');
  var editorConfig = $editor.data('config') || {};
  $editor.summernote(editorConfig);
});

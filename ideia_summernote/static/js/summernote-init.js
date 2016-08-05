$(function init() {
  var $editor = $(document).find('[data-toggle="editor"]');
  var editorConfig = $editor.data('config') || {};
  console.log(editorConfig);
  $editor.summernote(editorConfig);
});

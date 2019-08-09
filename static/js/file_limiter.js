// Checks how many images were selected on bug_report page
$('#id_images').change(function(){
    if(this.files.length>3){
        alert('Too many files');
        this.value = '';
    }
});
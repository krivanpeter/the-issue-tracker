$('#image-picker').click(function(){
    $("#id_images").click();
});
// Checks how many images were selected on bug_report page
$('#id_images').change(function(){
    if(this.files.length>3){
        alert('You can upload maximum 3 files');
        this.value = '';
    }
    else if(this.files.length == 1) {
        $('#number_of_chosen_files').html(this.files[0].name);
    }
    else{
        $('#number_of_chosen_files').html('Chosen files: ' + this.files.length);
    }
});


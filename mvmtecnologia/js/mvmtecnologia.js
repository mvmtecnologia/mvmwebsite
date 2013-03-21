$(document).ready(function() {

	$('#contatoForm').validate({
		rules : {
			inputName : {
				required : true,
			},
			inputEmail : {
				required : true,
				email : true
			},
			
			inputCity : {
				required : true,
			},
			
			inputComment : {
				required : true,
				maxlength:300,
			},
		 
		},
		messages : {
			inputName : {
				required : "O campo nome é obrigatorio.",
			},
			inputEmail : {
				required : "O campo email é obrigatorio.",
				email : "O campo email deve conter um email válido."
			},
			
			inputCity : {
				required : "O campo cidade é obrigatorio.",
			},
			
			inputComment : {
				required : "O campo comentário é obrigatorio.",
			}
		}

	});

});
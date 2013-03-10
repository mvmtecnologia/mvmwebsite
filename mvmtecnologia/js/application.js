/**
 * @author Marcus Vinicius Soliva
 * 
 * @author Matheus Cardoso
 */
$(document).ready(function() {

	$('#msgsuccess').hide();
	$('#msgaviso').hide();

	$('#enviarMsg').live('click', function() {

		var executeAction = true
 		var message = $('#message')
		var email = $('#email')
		var nome = $('#nome')

		$.each([ nome, email, message ], function(index, value) {
			if ($(value).val() == '') {

				$('#labelwanind').text("Por favor, preencha o campo " + $(value).attr('name'))
				$('#msgaviso').fadeIn(1000, function() {
					$('#msgaviso').fadeOut(4000);
				});
				executeAction = false
				return false
			}
		})

		if (executeAction) {
			$.post('/contato', {
				'message' : $(message).val(),
				'email' : $(email).val(),
				'nome' : $(nome).val()
			}, function() {
				$('#message').val('')
				$('#email').val('')
				$('#nome').val('')
				$('#msgsuccess').fadeIn(1000, function() {
					$('#msgsuccess').fadeOut(4000);
				});
			})

		}
	});

});
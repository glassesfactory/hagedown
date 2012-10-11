$(document).ready ()->
	$('a').live 'click', (event)->
		self = $(@)
		method = self.attr('data-method')
		if not method?
			return
		else
			event.preventDefault()

		url = self.attr('href')
		token = $('meta[name=_csrf_token]').attr('content')
		sendAjax(url, method, token)
		
	$('form').on 'submit', (event)->
		self = $(@)
		method = self.attr('method')
		
		if method isnt 'PUT' and method isnt 'put'
			return
		event.preventDefault()		
		url = self.attr('action')
		sendAjax(url, method, null, self.serializeArray())

	$success = $('.success')
	if $success?
		h = -$success.height() * 2
		setTimeout(()->
			$(window).on 'webkitTransitionEnd', (event)->
    			$('.alertArea').empty()
			$('.alert.success').css({
				'-webkit-transform':'translate3d(0,-60px,0)',
				'-webkit-transition':'400ms cubic-bezier(0,0,0.25,1)'
    		})
		,2000)
		$success.css({'-webkit-transform':'translate3d(0,0,0)','-webkit-transition':'500ms cubic-bezier(0,0,0.25,1)'})



sendAjax = (url, method, token, data)->
	if not data?
		data = []
	data.push({authenticity_token:token})
	$.ajax({
			url : url
			type : method
			data : data
			success : (data)->
				window.location.href = data
			error : (data)->
				console.log "faild"
		})

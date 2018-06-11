/*
 *
 * login-register modal
 * Autor: Creative Tim
 * Web-autor: creative.tim
 * Web script: http://creative-tim.com
 *
 */

function showGroupForm() {
    $('#loginModal .social, #div1, .loginBox, .registerBox, .login-footer').fadeOut('fast', function () {
        $('.groupBox, #div2, .register-footer').fadeIn('fast');
    });
    $('.modal-title').html('Which one are you?');
}

function showRegisterForm(objButton, group) {
    if (typeof(group) === 'undefined') {
        var fired_button = objButton.value;
    }
    else {
        var fired_button = group;
    }

    document.getElementById("next_val").value = fired_button;

    $('#facebook_login').each(function () {
        this.href += '?key=' + fired_button;
    });


    $('.loginBox, .groupBox').fadeOut('fast', function () {
        $('.registerBox, #loginModal .social, #div1').fadeIn('fast');
        $('.login-footer').fadeOut('fast', function () {
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('Register with');
    });
    $('.error').removeClass('alert alert-danger').html('');

}

function showLoginForm() {
    $('.registerBox, .groupBox').fadeOut('fast', function () {
        $('.loginBox, #loginModal .social, #div1').fadeIn('fast');
        $('.register-footer').fadeOut('fast', function () {
            $('.login-footer').fadeIn('fast');
        });

        $('.modal-title').html('Login with');
    });
    $('.error').removeClass('alert alert-danger').html('');
}

function openLoginModal() {
    showLoginForm();
    setTimeout(function () {
        $('#loginModal').modal('show');
    }, 230);

}

function openGroupModal() {
    showGroupForm();
    setTimeout(function () {
        $('#loginModal').modal('show');
    }, 230);
}

function openRegisterModal(objButton) {
    showRegisterForm(objButton, undefined);
    setTimeout(function () {
        $('#loginModal').modal('show');
    }, 230);
}

function loginAjax() {
    /*   Remove this comments when moving to server
    $.post( "/login", function( data ) {
            if(data == 1){
                window.location.replace("/home");
            } else {
                 shakeModal();
            }
        });
    */

    /*   Simulate error message from the server   */
    shakeModal();
}

function shakeModal() {
    $('#loginModal .modal-dialog').addClass('shake');
    $('.error').addClass('alert alert-danger').html("Invalid email/password combination");
    $('input[type="password"]').val('');
    setTimeout(function () {
        $('#loginModal .modal-dialog').removeClass('shake');
    }, 1000);
}

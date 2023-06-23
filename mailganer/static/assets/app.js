const validateEmail = function (email) {
    var formData = new FormData();
    formData.append('userEmail', email)
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/validate/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        error: function (xhr) {
            console.error(xhr.statusText);
        },
        success: function (res) {
            $('.error').text(res.msg);
        }
    });
};

const subscribeUser = function (email, username, firstName, lastName, birthDay) {
    var formData = new FormData();
    formData.append('userEmail', email);
    formData.append('userName', username);
    formData.append('userFirstName', firstName);
    formData.append('userLastName', lastName);
    formData.append('userBirthday', birthDay);
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/subscribe/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        error: function (xhr) {
            console.error(xhr.statusText);
        },
        success: function (res) {
            $('.success').text(res.msg);
            $('#userEmail').val(' ');
            $('#userName').val(' ');
            $('#userLastName').val(' ');
            $('#userFirstName').val(' ');
            $('#userBirthday').val(' ');
        }
    });
};

const massMailing = function (subject) {
     var formData = new FormData();
    formData.append('subject', subject);
    $.ajaxSetup({
        headers: {
            "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
        }
    });
    $.ajax({
        url: '/mass_mailing/',
        type: 'POST',
        dataType: 'json',
        cache: false,
        processData: false,
        contentType: false,
        data: formData,
        success: function (res) {
            $('.success').text(res.msg);
        }
    });
};

(function ($) {
    $('#submit').on('click', () => {
        event.preventDefault();
        const userEmail = $('#userEmail').val();
        const userName = $('#userName').val();
        const userFirstName = $('#userFirstName').val();
        const userLastName = $('#userLastName').val();
        const userBirthday = $('#userBirthday').val();
        if (userEmail && userName) {
            subscribeUser(userEmail, userName, userFirstName, userLastName, userBirthday);
        }
    });

    $('#submit1').on('click', () => {
        event.preventDefault();
        const subject = $('#subject').val();
        massMailing(subject);
    });

    $('#userEmail').on('change', (event) => {
        event.preventDefault();
        const email = event.target.value;
        validateEmail(email);
    });
})
(jQuery);
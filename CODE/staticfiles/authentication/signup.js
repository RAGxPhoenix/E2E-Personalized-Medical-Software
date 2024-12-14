document.addEventListener('DOMContentLoaded', function () {
    const doctorCheck = document.getElementById('doctorCheck');
    const medLicenseField = document.getElementById('medLicenseField');
    const specializationField = document.getElementById('specializationField');

    doctorCheck.addEventListener('change', function () {
        if (this.checked) {
            medLicenseField.style.display = 'blocked';
            specializationField.style.display = 'blocked';
        } else {
            medLicenseField.style.display = 'none';
            specializationField.style.display = 'none';
        }
    });
});


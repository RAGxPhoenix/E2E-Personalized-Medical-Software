function search() {
    var input = document.getElementById("searchInput").value;
    var doctorRows = document.querySelectorAll("#doctor-list tr");

    doctorRows.forEach(function(row) {
        var tagsCell = row.querySelector("td:nth-child(4)");
        if (tagsCell.textContent.toLowerCase().includes(input.toLowerCase())) {
            row.style.display = "";
        } else {
            row.style.display = "none";
        }
    });
}

document.addEventListener('DOMContentLoaded', function() {
    var doctors = [
      { name: "Dr. Jasmine Rivers", email: "jasmine.rivers@gmail.com", phone: "(555) 123-4567", tags: "Heart, Cardiovascular system", specialist: "Cardiologist" },
      { name: "Dr. Marcus Stone", email: "marcus.stone@gmail.com", phone: "(555) 234-5678", tags: "Skin, Hair, Nails", specialist: "Dermatologist" },
      { name: "Dr. Emily Parks", email: "emily.parks@gmail.com", phone: "(555) 345-6789", tags: "Stomach, Intestines, Digestive system", specialist: "Gastroenterologist" },
      { name: "Dr. Xavier Cruz", email: "xavier.cruz@gmail.com", phone: "(555) 456-7890", tags: "Brain, Nervses, Spinal Cord, Nervous System", specialist: "Neurologist" }, 
      { name: "Dr. Olivia Brooks", email: "olivia.brooks@gmail.com", phone: "(555) 567-8901", tags: "Eyes, Vision", specialist: "Ophthalmologist" },
      { name: "Dr. Nathan Reed", email: "nathan.reed@gmail.com", phone: "(555) 678-9012", tags: "Bones, Joints, Ligaments, Muscles", specialist: "Orthopedist" },
      { name: "Dr. Sophia Evans", email: "sophia.evans@gmail.com", phone: "(555) 789-0123", tags: "Ears, Nose, Throat", specialist: "Otolaryngologist (ENT)" },
      { name: "Dr. Carter Hughes", email: "carter.hughes@gmail.com", phone: "(555) 890-1234", tags: "Child health, Child Development", specialist: "Pediatrician" },
      { name: "Dr. Ava Foster", email: "ava.foster@gmail.com", phone: "(555) 901-2345", tags: "Mental health, Mental disorders", specialist: "Psychiatrist" },
      { name: "Dr. Elijah Martinez", email: "elijah.martinez@gmail.com", phone: "(555) 012-3456", tags: "Lungs, Respiratory system", specialist: "Pulmonologist" },
      { name: "Dr. Mia Thompson", email: "mia.thompson@gmail.com", phone: "(555) 123-4567", tags: "Joints, Muscles, Bones", specialist: "Rheumatologist" },
      { name: "Dr. Gabriel Ward", email: "gabriel.ward@gmail.com", phone: "(555) 234-5678", tags: "Kidneys, Bladder, Urinary tract system", specialist: "Urologist" },
      { name: "Dr. Isabella Barnes", email: "isabella.barnes@gmail.com", phone: "(555) 345-6789", tags: "Hormones, Glands, Endrocine System", specialist: "Endocrinologist" },
      { name: "Dr. Liam Wright", email: "liam.wright@gmail.com", phone: "(555) 456-7890", tags: "Blood", specialist: "Hematologist" },
      { name: "Dr. Harper Taylor", email: "harper.taylor@gmail.com", phone: "(555) 567-8901", tags: "Kidneys, Urinary system", specialist: "Nephrologist" },
      { name: "Dr. Zoe Mitchell", email: "zoe.mitchell@gmail.com", phone: "(555) 678-9012", tags: "Cancer diagnosis, Cancer treatment", specialist: "Oncologist" },
      { name: "Dr. Lucas Rodriguez", email: "lucas.rodriguez@gmail.com", phone: "(555) 789-0123", tags: "Allergic reactions, Immunity system", specialist: "Allergist/Immunologist" },
      { name: "Dr. Stella Campbell", email: "stella.campbell@gmail.com", phone: "(555) 890-1234", tags: "Diagnosis, Virus, Bacteria, Fungi, Infection", specialist: "Infectious Disease Specialist" },
      { name: "Dr. Noah Parker", email: "noah.parker@gmail.com", phone: "(555) 901-2345", tags: "Newborn health", specialist: "Neonatologist" },
      { name: "Dr. Lily Ramirez", email: "lily.ramirez@gmail.com", phone: "(555) 012-3456", tags: "Elderly care, Age health", specialist: "Geriatrician" },
      { name: "Dr. Ethan Cooper", email: "ethan.cooper@gmail.com", phone: "(555) 123-4567", tags: "Pregnancy, Childbirth", specialist: "Gynecologist" },
      { name: "Dr. Amelia Morgan", email: "amelia.morgan@gmail.com", phone: "(555) 234-5678", tags: "Anesthesia, Pain management", specialist: "Anesthesiologist" },
      { name: "Dr. Jackson Bennett", email: "jackson.bennett@gmail.com", phone: "(555) 345-6789", tags: "Diagnosis, Fluids, Tissues", specialist: "Pathlogist" },
      { name: "Dr. Scarlett Lopez", email: "scarlett.lopez@gmail.com", phone: "(555) 456-7890", tags: "X rays, CT scans, MRIs, Ultrasound", specialist: "Radiologist" },
      { name: "Dr. Aiden Kelly", email: "aiden.kelly@gmail.com", phone: "(555) 567-8901", tags: "Disability, Injury", specialist: "Physiatrist" },
    ];

    var doctorList = document.getElementById("doctor-list");

    doctors.forEach(function(doctor) {
      var row = document.createElement("tr");
      row.innerHTML = `
        <td>${doctor.name}</td>
        <td>${doctor.email}</td>
        <td>${doctor.phone}</td>
        <td>${doctor.tags}</td>
        <td>${doctor.specialist}</td>
      `;
      doctorList.appendChild(row);
    });
});

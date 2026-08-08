/* HealthMate AI - Main JavaScript */

// Dark Mode
function initDarkMode() {
  const saved = localStorage.getItem('hm-theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
  const btn = document.getElementById('darkToggle');
  if (btn) btn.classList.toggle('on', saved === 'dark');
}

function toggleDark() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('hm-theme', next);
  const btn = document.getElementById('darkToggle');
  if (btn) btn.classList.toggle('on', next === 'dark');
}

// Language Translation Engine
const TRANSLATIONS = {
  en: {
    brand_sub: "Diabetes Prediction",
    nav_main: "Main",
    nav_dashboard: "Dashboard",
    nav_predict: "New Prediction",
    nav_history: "History",
    nav_health: "Health",
    nav_diet: "Diet Plans",
    nav_analytics: "Analytics",
    nav_account: "Account",
    nav_profile: "Profile",
    nav_admin: "Admin",
    nav_logout: "Logout",
    user_role: "Patient",
    btn_new_test: "New Test",
    page_dashboard: "Dashboard Overview",
    page_predict: "Diabetes Risk Assessment",
    page_result: "Assessment Result",
    page_diet: "Diet Recommendations",
    page_analytics: "Health Analytics",
    page_profile: "User Profile",
    page_history: "Prediction History",
    form_sec1_title: "Reproductive History",
    form_sec1_sub: "Enter 0 if not applicable",
    form_pregnancies: "Pregnancies",
    form_age: "Age (years)",
    form_sec2_title: "Blood Parameters",
    form_sec2_sub: "From your latest lab report",
    form_glucose: "Glucose Level",
    form_insulin: "Insulin Level",
    form_bp: "Blood Pressure",
    form_skin: "Skin Thickness",
    form_sec3_title: "Body Metrics",
    form_weight: "Weight (kg)",
    form_height: "Height (cm)",
    form_bmi: "BMI",
    form_pedigree: "Diabetes Pedigree Function",
    btn_submit_pred: "Run AI Prediction",
    res_risk_score: "Risk Score",
    res_diagnosis: "Diagnosis",
    res_diabetic: "Diabetic Risk Detected",
    res_nondiabetic: "Low Risk / Normal",
    btn_download_pdf: "Download PDF Report",
    diet_title: "Personalized Diet Recommendations",
    diet_breakfast: "🌅 Breakfast Options",
    diet_lunch: "☀️ Lunch Options",
    diet_dinner: "🌙 Dinner Options",
    diet_snacks: "🍎 Healthy Snacks",
    diet_tips: "💡 Health Tips",
    foods_to_eat: "🥦 Foods to Eat",
    foods_to_avoid: "🚫 Foods to Avoid",
    total_tests: "Total Tests",
    latest_result: "Latest Result",
    avg_glucose: "Average Glucose",
    avg_bp: "Average BP",
    recent_activity: "Recent Activity",
    quick_actions: "Quick Actions",
    home_hero_title: "AI-Powered Diabetes Risk Prediction & Diet Planner",
    home_hero_sub: "Instant health risk assessment using Machine Learning and customized diet recommendations tailored for you.",
    btn_start_test: "Start Assessment",
    btn_view_demo: "View Dashboard"
  },
  hi: {
    brand_sub: "मधुमेह का पूर्वानुमान",
    nav_main: "मुख्य",
    nav_dashboard: "डैशबोर्ड",
    nav_predict: "नया परीक्षण",
    nav_history: "इतिहास",
    nav_health: "स्वास्थ्य",
    nav_diet: "आहार योजनाएं",
    nav_analytics: "विश्लेषण",
    nav_account: "खाता",
    nav_profile: "प्रोफाइल",
    nav_admin: "एडमिन",
    nav_logout: "लॉगआउट",
    user_role: "रोगी (Patient)",
    btn_new_test: "नया टेस्ट",
    page_dashboard: "डैशबोर्ड अवलोकन",
    page_predict: "मधुमेह जोखिम मूल्यांकन",
    page_result: "मूल्यांकन परिणाम",
    page_diet: "आहार सिफारिशें",
    page_analytics: "स्वास्थ्य विश्लेषण",
    page_profile: "उपयोगकर्ता प्रोफाइल",
    page_history: "पूर्व परीक्षण इतिहास",
    form_sec1_title: "प्रजनन इतिहास",
    form_sec1_sub: "लागू न होने पर 0 दर्ज करें",
    form_pregnancies: "गर्भावस्था संख्या",
    form_age: "आयु (वर्ष)",
    form_sec2_title: "रक्त पैरामीटर",
    form_sec2_sub: "अपनी नवीनतम लैब रिपोर्ट से",
    form_glucose: "ग्लूकोज स्तर (mg/dL)",
    form_insulin: "इंसुलिन स्तर (mu U/ml)",
    form_bp: "रक्तचाप (mmHg)",
    form_skin: "त्वचा की मोटाई (mm)",
    form_sec3_title: "शरीर के माप (Body Metrics)",
    form_weight: "वजन (किलोग्राम)",
    form_height: "ऊंचाई (सेमी)",
    form_bmi: "बीएमआई (BMI)",
    form_pedigree: "मधुमेह वंशावली स्कोर",
    btn_submit_pred: "एआई परीक्षण चलाएं",
    res_risk_score: "जोखिम स्कोर",
    res_diagnosis: "निदान (Diagnosis)",
    res_diabetic: "मधुमेह का जोखिम पाया गया",
    res_nondiabetic: "कम जोखिम / सामान्य",
    btn_download_pdf: "पीडीएफ रिपोर्ट डाउनलोड करें",
    diet_title: "व्यक्तिगत आहार सिफारिशें",
    diet_breakfast: "🌅 नाश्ता",
    diet_lunch: "☀️ दोपहर का खाना",
    diet_dinner: "🌙 रात का खाना",
    diet_snacks: "🍎 स्वस्थ स्नैक्स",
    diet_tips: "💡 स्वास्थ्य सुझाव",
    foods_to_eat: "🥦 खाने योग्य भोजन",
    foods_to_avoid: "🚫 परहेज करने योग्य भोजन",
    total_tests: "कुल परीक्षण",
    latest_result: "नवीनतम परिणाम",
    avg_glucose: "औसत ग्लूकोज",
    avg_bp: "औसत रक्तचाप",
    recent_activity: "हाल की गतिविधि",
    quick_actions: "त्वरित कार्रवाई",
    home_hero_title: "एआई-संचालित मधुमेह जोखिम पूर्वानुमान और आहार योजनाकार",
    home_hero_sub: "मशीन लर्निंग द्वारा त्वरित स्वास्थ्य जोखिम मूल्यांकन और आपके लिए विशेष आहार सुझाव।",
    btn_start_test: "मूल्यांकन शुरू करें",
    btn_view_demo: "डैशबोर्ड देखें"
  },
  te: {
    brand_sub: "మధుమేహ అంచనా",
    nav_main: "ప్రధానం",
    nav_dashboard: "డాష్‌బోర్డ్",
    nav_predict: "కొత్త పరీక్ష",
    nav_history: "చరిత్ర",
    nav_health: "ఆరోగ్యం",
    nav_diet: "డైట్ ప్లాన్‌లు",
    nav_analytics: "విశ్లేషణ",
    nav_account: "ఖాతా",
    nav_profile: "ప్రొఫైల్",
    nav_admin: "అడ్మిన్",
    nav_logout: "లాగ్‌అవుట్",
    user_role: "పేషెంట్ (Patient)",
    btn_new_test: "కొత్త టెస్ట్",
    page_dashboard: "డాష్‌బోర్డ్ వివరణ",
    page_predict: "మధుమేహ అంచనా పరీక్ష",
    page_result: "పరీక్ష ఫలితం",
    page_diet: "డైట్ సూచనలు",
    page_analytics: "ఆరోగ్య విశ్లేషణలు",
    page_profile: "యూజర్ ప్రొఫైల్",
    page_history: "గత పరీక్షల చరిత్ర",
    form_sec1_title: "గర్భధారణ చరిత్ర",
    form_sec1_sub: "వర్తించకపోతే 0 నమోదు చేయండి",
    form_pregnancies: "గర్భధారణ సంఖ్య",
    form_age: "వయస్సు (సంవత్సరాలు)",
    form_sec2_title: "రక్త పరీక్ష వివరాలు",
    form_sec2_sub: "మీ తాజా ల్యాబ్ రిపోర్ట్ నుండి",
    form_glucose: "గ్లూకోజ్ స్థాయి (mg/dL)",
    form_insulin: "ఇన్సులిన్ స్థాయి (mu U/ml)",
    form_bp: "రక్తపోటు (mmHg)",
    form_skin: "చర్మం మందం (mm)",
    form_sec3_title: "శరీర కొలతలు (Body Metrics)",
    form_weight: "బరువు (కేజీలు)",
    form_height: "ఎత్తు (సెంటీమీటర్లు)",
    form_bmi: "BMI (బిఎమ్‌ఐ)",
    form_pedigree: "మధుమేహ పెడిగ్రీ స్కోరు",
    btn_submit_pred: "AI పరీక్ష ప్రారంభించండి",
    res_risk_score: "ప్రమాద స్కోరు",
    res_diagnosis: "రోగనిర్ధారణ",
    res_diabetic: "మధుమేహం ప్రమాదం గుర్తించబడింది",
    res_nondiabetic: "తక్కువ ప్రమాదం / సాధారణం",
    btn_download_pdf: "PDF నివేదిక డౌన్‌లోడ్ చేయండి",
    diet_title: "వ్యక్తిగత డైట్ సూచనలు",
    diet_breakfast: "🌅 అల్పాహారం",
    diet_lunch: "☀️ మధ్యాహ్న భోజనం",
    diet_dinner: "🌙 రాత్రి భోజనం",
    diet_snacks: "🍎 ఆరోగ్యకరమైన స్నాక్స్",
    diet_tips: "💡 ఆరోగ్య సూచనలు",
    foods_to_eat: "🥦 తినవలసిన పదార్థాలు",
    foods_to_avoid: "🚫 నివారించాల్సిన పదార్థాలు",
    total_tests: "మొత్తం పరీక్షలు",
    latest_result: "తాజా ఫలితం",
    avg_glucose: "సగటు గ్లూకోజ్",
    avg_bp: "సగటు రక్తపోటు",
    recent_activity: "ఇటీవలి సమాచారం",
    quick_actions: "త్వరిత చర్యలు",
    home_hero_title: "AI ఆధారిత మధుమేహ అంచనా & డైట్ ప్లానర్",
    home_hero_sub: "మెషిన్ లెర్నింగ్ ద్వారా మీ ఆరోగ్య ప్రమాద అంచనా మరియు సూచించిన డైట్ ప్లాన్.",
    btn_start_test: "పరీక్ష ప్రారంభించండి",
    btn_view_demo: "డాష్‌బోర్డ్ చూడండి"
  }
};

function setGoogleTranslateCookie(lang) {
  const cookieVal = '/en/' + lang;
  document.cookie = 'googtrans=' + cookieVal + '; path=/;';
  document.cookie = 'googtrans=' + cookieVal + '; domain=' + window.location.hostname + '; path=/;';
  
  const select = document.querySelector('.goog-te-combo');
  if (select) {
    select.value = lang;
    select.dispatchEvent(new Event('change'));
  }
}

function applyLanguage(lang) {
  const dict = TRANSLATIONS[lang] || TRANSLATIONS['en'];
  document.querySelectorAll('[data-i18n]').forEach(el => {
    const key = el.dataset.i18n;
    if (dict[key]) {
      const icon = el.querySelector('i, svg');
      if (icon) {
        el.innerHTML = icon.outerHTML + ' ' + dict[key];
      } else {
        el.textContent = dict[key];
      }
    }
  });
  document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
    const key = el.dataset.i18nPlaceholder;
    if (dict[key]) el.placeholder = dict[key];
  });
  document.querySelectorAll('[data-lang]').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.lang === lang);
  });
  setGoogleTranslateCookie(lang);
}

function setLanguage(lang) {
  localStorage.setItem('hm-lang', lang);
  applyLanguage(lang);
  fetch('/accounts/set-language/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken') },
    body: JSON.stringify({ language: lang })
  }).catch(() => {});
  setTimeout(() => {
    location.reload();
  }, 150);
}

function initLanguage() {
  const lang = localStorage.getItem('hm-lang') || 'en';
  applyLanguage(lang);
}

// Sidebar
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const overlay = document.getElementById('sidebarOverlay');
  sidebar?.classList.toggle('open');
  overlay?.classList.toggle('open');
}

// Cookie helper
function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (let c of cookies) {
    const [k, v] = c.trim().split('=');
    if (k === name) return decodeURIComponent(v);
  }
  return null;
}

// Auto-dismiss alerts
function initAlerts() {
  document.querySelectorAll('.auto-dismiss').forEach(el => {
    setTimeout(() => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(-10px)';
      setTimeout(() => el.remove(), 300);
    }, 4000);
  });
}

// Animate numbers
function animateNumber(el) {
  const target = parseFloat(el.dataset.target || el.textContent);
  const isFloat = String(target).includes('.');
  const decimals = isFloat ? 1 : 0;
  const duration = 1200;
  const step = target / (duration / 16);
  let current = 0;
  const timer = setInterval(() => {
    current = Math.min(current + step, target);
    el.textContent = isFloat ? current.toFixed(decimals) : Math.floor(current);
    if (current >= target) clearInterval(timer);
  }, 16);
}

function initCounters() {
  document.querySelectorAll('[data-counter]').forEach(el => {
    const obs = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { animateNumber(el); obs.unobserve(el); } });
    });
    obs.observe(el);
  });
}

// Progress bars animation
function initProgress() {
  document.querySelectorAll('.progress-bar[data-width]').forEach(bar => {
    const obs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          bar.style.width = bar.dataset.width + '%';
          obs.unobserve(bar);
        }
      });
    });
    obs.observe(bar);
  });
}

// Animate elements in
function initAnimations() {
  document.querySelectorAll('.anim').forEach((el, i) => {
    el.style.opacity = '0';
    const obs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          setTimeout(() => {
            el.style.animation = `fadeInUp 0.5s ease both`;
            el.style.opacity = '';
          }, (i % 6) * 80);
          obs.unobserve(el);
        }
      });
    }, { threshold: 0.1 });
    obs.observe(el);
  });
}

// BMI Calculator
function calculateBMI() {
  const weight = parseFloat(document.getElementById('bmiWeight')?.value);
  const heightCm = parseFloat(document.getElementById('bmiHeight')?.value);
  if (weight && heightCm) {
    const heightM = heightCm / 100;
    const bmi = (weight / (heightM * heightM)).toFixed(1);
    const bmiField = document.getElementById('id_bmi');
    if (bmiField) bmiField.value = bmi;
    
    const display = document.getElementById('bmiDisplay');
    if (display) {
      let status, cls;
      if (bmi < 18.5) { status = 'Underweight'; cls = 'warning'; }
      else if (bmi < 25) { status = 'Normal'; cls = 'normal'; }
      else if (bmi < 30) { status = 'Overweight'; cls = 'warning'; }
      else { status = 'Obese'; cls = 'danger'; }
      display.innerHTML = `<span class="hbadge ${cls}">BMI: ${bmi} — ${status}</span>`;
    }
  }
}

// Risk gauge
function drawGauge(canvasId, value, max = 100) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) return;
  const ctx = canvas.getContext('2d');
  const cx = canvas.width / 2;
  const cy = canvas.height * 0.85;
  const radius = Math.min(canvas.width, canvas.height) * 0.7;
  
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Background arc
  ctx.beginPath();
  ctx.arc(cx, cy, radius, Math.PI, 0);
  ctx.lineWidth = 18;
  ctx.strokeStyle = '#e2e8f0';
  ctx.lineCap = 'round';
  ctx.stroke();
  
  // Value arc
  const pct = value / max;
  const color = pct < 0.3 ? '#10b981' : pct < 0.6 ? '#f59e0b' : '#ef4444';
  ctx.beginPath();
  ctx.arc(cx, cy, radius, Math.PI, Math.PI + pct * Math.PI);
  ctx.strokeStyle = color;
  ctx.stroke();
  
  // Center text
  ctx.fillStyle = color;
  ctx.font = 'bold 28px Outfit, sans-serif';
  ctx.textAlign = 'center';
  ctx.fillText(value.toFixed(1) + '%', cx, cy - 10);
  
  ctx.fillStyle = '#64748b';
  ctx.font = '12px Outfit, sans-serif';
  ctx.fillText('Risk Score', cx, cy + 12);
}

// Initialize charts helper
function createLineChart(id, labels, datasets, title = '') {
  const canvas = document.getElementById(id);
  if (!canvas) return;
  
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  const gridColor = isDark ? 'rgba(255,255,255,0.07)' : 'rgba(0,0,0,0.06)';
  const textColor = isDark ? '#94a3b8' : '#64748b';
  
  return new Chart(canvas, {
    type: 'line',
    data: { labels, datasets },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: textColor, font: { family: 'Outfit', size: 12 }, boxWidth: 14 } },
        title: title ? { display: true, text: title, color: textColor } : { display: false },
        tooltip: {
          backgroundColor: isDark ? '#1e293b' : '#0f172a',
          titleColor: '#fff', bodyColor: '#94a3b8',
          borderColor: 'rgba(255,255,255,0.1)', borderWidth: 1,
          cornerRadius: 8, padding: 10,
        }
      },
      scales: {
        x: { grid: { color: gridColor }, ticks: { color: textColor, font: { family: 'Outfit', size: 11 } } },
        y: { grid: { color: gridColor }, ticks: { color: textColor, font: { family: 'Outfit', size: 11 } } },
      },
      elements: { line: { tension: 0.4 }, point: { radius: 4, hoverRadius: 6 } }
    }
  });
}

function createBarChart(id, labels, data, color = '#1a56db') {
  const canvas = document.getElementById(id);
  if (!canvas) return;
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  const gridColor = isDark ? 'rgba(255,255,255,0.07)' : 'rgba(0,0,0,0.06)';
  const textColor = isDark ? '#94a3b8' : '#64748b';
  
  return new Chart(canvas, {
    type: 'bar',
    data: {
      labels,
      datasets: [{
        data,
        backgroundColor: color + '33',
        borderColor: color,
        borderWidth: 2,
        borderRadius: 8,
        borderSkipped: false,
      }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      plugins: { legend: { display: false } },
      scales: {
        x: { grid: { display: false }, ticks: { color: textColor } },
        y: { grid: { color: gridColor }, ticks: { color: textColor } }
      }
    }
  });
}

function createDoughnutChart(id, labels, data, colors) {
  const canvas = document.getElementById(id);
  if (!canvas) return;
  const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
  
  return new Chart(canvas, {
    type: 'doughnut',
    data: {
      labels,
      datasets: [{ data, backgroundColor: colors, borderWidth: 0, hoverOffset: 6 }]
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      cutout: '72%',
      plugins: {
        legend: {
          position: 'bottom',
          labels: { color: isDark ? '#94a3b8' : '#64748b', padding: 16, font: { family: 'Outfit', size: 12 }, boxWidth: 12, usePointStyle: true }
        }
      }
    }
  });
}

// On DOM ready
document.addEventListener('DOMContentLoaded', () => {
  initDarkMode();
  initLanguage();
  initAlerts();
  initCounters();
  initProgress();
  initAnimations();
  
  // Sidebar toggle
  document.getElementById('sidebarToggle')?.addEventListener('click', toggleSidebar);
  document.getElementById('sidebarOverlay')?.addEventListener('click', toggleSidebar);
  document.getElementById('darkToggle')?.addEventListener('click', toggleDark);
  
  // Lang buttons
  document.querySelectorAll('[data-lang]').forEach(btn => {
    btn.addEventListener('click', () => setLanguage(btn.dataset.lang));
  });
  
  // BMI calculator
  document.getElementById('bmiWeight')?.addEventListener('input', calculateBMI);
  document.getElementById('bmiHeight')?.addEventListener('input', calculateBMI);
  
  // Mark active nav
  const path = window.location.pathname;
  document.querySelectorAll('.sidebar-nav .nav-link').forEach(link => {
    if (link.getAttribute('href') && path.startsWith(link.getAttribute('href')) && link.getAttribute('href') !== '/') {
      link.classList.add('active');
    }
  });
});

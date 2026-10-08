// ===== Navbar: shrink/blur on scroll + back-to-top button =====
const nav = document.getElementById('nav'), topBtn = document.getElementById('top');
addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', scrollY > 40);
  topBtn.classList.toggle('show', scrollY > 500);
}, { passive: true });
topBtn.onclick = () => scrollTo({ top: 0, behavior: 'smooth' });

// ===== Mobile hamburger menu =====
const burger = document.getElementById('burger'), menu = document.getElementById('menu');
const setMenu = open => { menu.classList.toggle('open', open); burger.classList.toggle('open', open); burger.setAttribute('aria-expanded', open); };
burger.onclick = () => setMenu(!menu.classList.contains('open'));
menu.querySelectorAll('a').forEach(a => a.onclick = () => setMenu(false));

// ===== Typing effect (roles come from app.py) =====
const typed = document.getElementById('typed'), roles = JSON.parse(typed.dataset.roles);
let r = 0, c = 0, del = false;
(function type() {
  const w = roles[r];
  if (!del) { c++; typed.textContent = w.slice(0, c); if (c === w.length) { del = true; return setTimeout(type, 1400); } }
  else { c--; typed.textContent = w.slice(0, c); if (c === 0) { del = false; r = (r + 1) % roles.length; } }
  setTimeout(type, del ? 40 : 80);
})();

// ===== Scroll reveal =====
const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('show'); io.unobserve(e.target); } }), { threshold: .12 });
document.querySelectorAll('.reveal').forEach(el => io.observe(el));

// ===== Highlight active nav link =====
const links = [...menu.querySelectorAll('a')];
const spy = new IntersectionObserver(es => es.forEach(e => {
  if (e.isIntersecting) links.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id));
}), { rootMargin: '-45% 0px -50% 0px' });
document.querySelectorAll('main section[id]').forEach(s => spy.observe(s));

// ===== Project filter =====
document.querySelectorAll('.filter').forEach(b => b.onclick = () => {
  document.querySelectorAll('.filter').forEach(x => x.classList.remove('active'));
  b.classList.add('active');
  document.querySelectorAll('.project').forEach(p =>
    p.classList.toggle('hide', b.dataset.filter !== 'All' && p.dataset.cat !== b.dataset.filter));
});

// ===== Contact form: validation, then opens the visitor's email app (no server email) =====
const form = document.getElementById('form'), note = document.getElementById('note');
form.addEventListener('submit', e => {
  e.preventDefault();
  let ok = true;
  form.querySelectorAll('label').forEach(l => {
    const f = l.querySelector('input,textarea'), err = l.querySelector('.err');
    let msg = '';
    if (!f.value.trim()) msg = 'This field is required.';
    else if (f.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value)) msg = 'Enter a valid email.';
    else if (f.minLength > 0 && f.value.trim().length < f.minLength) msg = `Minimum ${f.minLength} characters.`;
    err.textContent = msg; l.classList.toggle('bad', !!msg); if (msg) ok = false;
  });
  if (!ok) return;
  const d = new FormData(form);
  const body = `${d.get('message')}\n\nFrom: ${d.get('name')} (${d.get('email')})`;
  location.href = `mailto:adityashinde8742@gmail.com?subject=${encodeURIComponent(d.get('subject'))}&body=${encodeURIComponent(body)}`;
  note.textContent = 'Opening your email app to send this message…';
});

document.getElementById('year').textContent = new Date().getFullYear();

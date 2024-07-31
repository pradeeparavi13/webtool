/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: [
    './myproject/**/*.html',
    './myproject/**/*.js',
    './myproject/**/*.py',
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
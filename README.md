<h1>Polynomial Partial Fraction Decomposition Tool</h1>

<p>This Python project performs partial fraction decomposition on rational polynomials. It was created by Wissam Nusair, inspired by Dr. Sauer, with code comments by Claude 3.5 Sonnet.</p>

<h2>Features</h2>
<ul>
  <li>Interactive input for polynomial coefficients</li>
  <li>Supports polynomials of any degree for both numerator and denominator</li>
  <li>Utilizes SymPy for symbolic mathematics operations</li>
  <li>Performs partial fraction decomposition</li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>Python 3.10 or higher</li>
  <li>SymPy library</li>
</ul>

<h2>Installation</h2>
<p>This project uses Poetry for dependency management. To install the required packages, run:</p>
<pre><code>poetry install</code></pre>

<h2>Usage</h2>
<ol>
  <li>Run the script:</li>
  <pre><code>python main.py</code></pre>

  <li>Enter the degree of the numerator polynomial when prompted.</li>

  <li>Enter the degree of the denominator polynomial when prompted.</li>

  <li>Input the coefficients for each term of the numerator polynomial, starting from the lowest degree (x^0) to the highest.</li>

  <li>Input the coefficients for each term of the denominator polynomial, following the same order.</li>

  <li>The program will output the partial fraction decomposition of your rational polynomial.</li>
</ol>

<h2>Example</h2>
<p>For the rational polynomial (2x^2 + 3x + 1) / (x^2 - 1), you would input:</p>
<pre><code>
Enter the degree of the polynomial's numerator: 2
Enter the degree of the polynomial's denominator: 2

What is the numerator coefficient of x^0? 1
What is the numerator coefficient of x^1? 3
What is the numerator coefficient of x^2? 2

What is the denominator coefficient of x^0? -1
What is the denominator coefficient of x^1? 0
What is the denominator coefficient of x^2? 1
</code></pre>

<h2>How It Works</h2>
<ol>
  <li>The script uses SymPy's <code>symbols</code> to create a symbolic variable 'x'.</li>
  <li>It collects user input for polynomial coefficients.</li>
  <li>Constructs the numerator and denominator polynomials using the input coefficients.</li>
  <li>Creates a rational polynomial by dividing the numerator by the denominator.</li>
  <li>Uses SymPy's <code>apart</code> function to perform partial fraction decomposition.</li>
  <li>Prints the result of the decomposition.</li>
</ol>

<h2>Contributing</h2>
<p>Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.</p>

<h2>License</h2>
<p>This project is open source and available under the MIT License.</p>
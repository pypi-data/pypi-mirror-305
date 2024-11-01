const supportsColors = false;
const chalk = {
  boldRed: (text) => supportsColors ? `\x1b[1m\x1b[91m${text}\x1b[0m` : text,
  blueBright: (text) => supportsColors ? `\x1b[91m${text}\x1b[0m` : text,
  dim: (text) => supportsColors ? `\x1b[2m${text}\x1b[0m` : text,
  red: (text) => supportsColors ? `\x1b[91m${text}\x1b[0m` : text,
  bold: (text) => supportsColors ? `\x1b[1m${text}\x1b[0m` : text,
};
const fs = require('fs');
/**
 * Formats a given line by applying syntax highlighting
 *  for specific statements and symbols.
 *
 * @param {string} line - The input line to be formatted.
 * @return {string} - The formatted line with applied syntax highlighting.
 */
function formatLine(line) {
  const statements = [
    'const ', 'await ', 'import ', 'let ',
    'var ', 'async ', 'self ', 'def ', 'return ',
    'from ', 'for ', 'with ', 'raise ', 'try ',
    'except ', 'catch ', 'elif ', 'if ',
    ':', '\\(', '\\)', '\\+', '\\-', '\\*', '='];
  const secondary = ['{', '}', '\'', ' true', ' false'];
  for (const statement of statements) {
    line = line.replace(
        new RegExp(statement, 'g'),
        chalk.red(statement.replace('\\', '')) + '');
  }
  for (const second of secondary) {
    line = line.replace(
        new RegExp(second, 'g'),
        chalk.blueBright(second) + '');
  }
  return line;
}

/**
 * Prints an error message with detailed information
 * from both JavaScript and Python stack traces.
 *
 * @param {string} failedCall - The name of the failed function call.
 * @param {string} jsErrorline - The JavaScript error line.
 * @param {string[]} jsStacktrace - The JavaScript stack trace.
 * @param {string} pyErrorline - The Python error line.
 * @param {Array<[string, string]>} pyStacktrace - The Python stack trace.
 * @return {string[]} - An array of formatted lines for the error message.
 */
function printError(
    failedCall, jsErrorline, jsStacktrace, pyErrorline, pyStacktrace) {
  const lines = [];
  const log = (...sections) => lines.push(sections.join(' '));
  console.log('FAILAT', jsErrorline, jsStacktrace, pyErrorline, pyStacktrace);
  log('Python:',
      chalk.boldRed(' Python Error '),
      `JavaScript attempt to call '${
        failedCall.replace('~~', '') || 'some function'
      }' in Python failed:`,
  );
  log(chalk.dim('>'), formatLine(jsErrorline.trim()));

  for (const traceline of jsStacktrace) {
    log(' ', chalk.dim(traceline));
  }

  log('\n... [Context: Python] ...\n');

  for (const [at, line] of pyStacktrace) {
    if (at.includes('javascriptasync')) continue;
    if (!line) {
      log(' ', chalk.dim(at));
    } else {
      log(chalk.dim('>'), formatLine(line.trim()));
      log(' ', chalk.dim(at));
    }
  }
  log('Bridge PY:', chalk.bold(pyErrorline));
  return lines;
}

/**
 * Processes a Python stack trace and extracts relevant information.
 *
 * @param {string} pyTrace - The raw Python stack trace.
 * @return {[string, Array<[string]>]} - A tuple containing the Python
 * error line and stack trace lines.
 */
function processPyStacktrace(pyTrace) {
  const pyTraceLines = [];
  let pyErrorLine = '';
  for (const lin of pyTrace.split('\n')) {
    if (lin.startsWith('  File')) {
      const fname = lin.split('"')[1];
      const line = lin.match(/, line (\d+)/)[1];
      const at = lin.match(/, in (.*)/)?.[1] ?? '^';
      pyTraceLines.push([`at ${at} (${fname}:${line})`]);
    } else if (lin.startsWith('    ')) {
      pyTraceLines[pyTraceLines.length - 1]?.push(lin.trim());
    } else if (lin.trim()) {
      pyErrorLine = lin.trim();
    }
  }
  return [pyErrorLine, pyTraceLines];
}

const INTERNAL_FILES = [
  'bridge.js', 'pyi.js', 'errors.js', 'deps.js', 'test.js',
];

const isInternal = (file) => INTERNAL_FILES.find((k) => file.includes(k));

/**
 * Processes a JavaScript stack trace and extracts relevant information.
 *
 * @param {string[]} stack - The raw JavaScript stack trace.
 * @param {boolean} [allowInternal=false] - Flag to allow internal files
 * in the stack trace.
 * @return {?[string, string[]]} - A tuple containing
 * the JavaScript error line and stack trace lines, or null if not found.
 */
function processJSStacktrace(stack, allowInternal) {
  const jsTraceLines = [];
  let jsErrorline;
  let foundMainLine = false;
  for (const line of stack.split('\n')) {
    if (!(isInternal(line) && !allowInternal) && !foundMainLine) {
      const absPath = line.match(/\((.*):(\d+):(\d+)\)/);
      const filePath = line.match(/(file:\/\/.*):(\d+):(\d+)/);
      const barePath = line.match(/at (.*):(\d+):(\d+)$/);
      const path = absPath || filePath || barePath;
      if (path) {
        // eslint-disable-next-line no-unused-vars
        const [fpath, errline, char] = path.slice(1);
        if (fpath.startsWith('node:') || fpath.startsWith('internal/')) {
          continue;
        }
        const file = fs.readFileSync(
          fpath.startsWith('file:') ? new URL(fpath) : fpath, 'utf-8',
        );
        const flines = file.split('\n');
        jsErrorline = flines[errline - 1];
        jsTraceLines.push(line.trim());
        foundMainLine = true;
      }
    } else if (foundMainLine) {
      jsTraceLines.push(line.trim());
    }
  }
  return jsErrorline ? [jsErrorline, jsTraceLines] : null;
}

/**
 * Generates an error message by combining information
 *  from JavaScript and Python stack traces.
 *
 * @param {string} failedCall - The name of the failed function call.
 * @param {string} jsStacktrace - The JavaScript stack trace.
 * @param {string} pyStacktrace - The Python stack trace.
 * @return {string} - The formatted error message.
 */
function getErrorMessage(failedCall, jsStacktrace, pyStacktrace) {
  try {
    const [jse, jss] =
       processJSStacktrace(jsStacktrace) ||
       processJSStacktrace(jsStacktrace, true);
    const [pye, pys] = processPyStacktrace(pyStacktrace);

    const lines = printError(failedCall, jse, jss, pye, pys);
    return lines.join('\n');
  } catch (e) {
    console.error('** Error in exception handler **', e);
    const tracea=`** JavaScript Stacktrace **\n${jsStacktrace}\n**`;
    const traceb=`Python Stacktrace **\n${pyStacktrace}`;
    console.log(
        `fal ${tracea}\n${traceb}`,
    );
    return '';
  }
}

module.exports = {getErrorMessage};

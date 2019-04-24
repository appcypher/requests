
class Timer {
  constructor(fn, time) {
    this.fn = fn;
    this.timeout = setTimeout(fn, time);
  }

  extend(time) {
    clearTimeout(this.timeout);
    this.timeout = setTimeout(this.fn, time);
  }

  stop() {
    clearTimeout(this.timeout);
    this.timeout = null;
  }

  restart(time) {
    this.timeout = setTimeout(this.fn, time);
  }
}

export default Timer;

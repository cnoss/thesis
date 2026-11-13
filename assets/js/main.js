import { finishedWorks, showAdditionalWorks } from './modules/finished-works.js';
import { stateOfWorkIndicator } from './modules/state-of-works-indicator.js';
import { slideshow } from './modules/slideshow.js';
import { pageTransitions } from './modules/page-transitions.js';

/* Main
############################################################################ */

pageTransitions();

document.addEventListener('DOMContentLoaded', function() {
  hljs.highlightAll();
  finishedWorks();
  stateOfWorkIndicator();
  slideshow();
});
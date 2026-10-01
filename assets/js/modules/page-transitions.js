/* Page Transitions
############################################################################ */

// Beim Verlassen der Übersicht bekommt nur das Thumbnail der angeklickten Arbeit
// den Namen „work-thumbnail“, damit es in das Bild der Detailseite übergeht.
// Browser ohne Cross-Document View Transitions feuern „pageswap“ nicht.
const thumbnailName = "work-thumbnail";

export const pageTransitions = () => {
  window.addEventListener("pageswap", (event) => {
    if (!event.viewTransition || !event.activation?.entry?.url) return;

    const targetUrl = new URL(event.activation.entry.url);
    const links = document.querySelectorAll(".work-item a[href]");
    const link = [...links].find((a) => new URL(a.href).pathname === targetUrl.pathname);
    const image = link?.querySelector("img");
    if (!image) return;

    image.style.viewTransitionName = thumbnailName;
    event.viewTransition.finished.finally(() => {
      image.style.viewTransitionName = "";
    });
  });
};

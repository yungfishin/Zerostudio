// ZeroStudio Service Worker (PWA Offline Shell Engine)
const CACHE_NAME = 'zerostudio-cache-v2.4.0';
const STATIC_ASSETS = [
    './',
    './index.html',
    './app.js',
    './libs/i18n.js',
    './manifest.json',
    './version.json',
    './assets/icons/icon-192.png',
    './assets/icons/icon-512.png',
    './assets/icons/favicon.png',
    './assets/images/zerostudio-og-preview.png'
];

self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(STATIC_ASSETS);
        }).then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(
                keys.map((key) => {
                    if (key !== CACHE_NAME) {
                        return caches.delete(key);
                    }
                })
            );
        }).then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', (event) => {
    const url = new URL(event.request.url);

    // CRITICAL: NEVER cache API bridge or WASM license validation calls
    if (url.pathname.startsWith('/api') || url.port === '8900' || event.request.method !== 'GET') {
        return;
    }

    // Network-First with Cache Fallback for shell assets
    event.respondWith(
        fetch(event.request)
            .then((networkResponse) => {
                // If valid response, update cache in background
                if (networkResponse && networkResponse.status === 200 && networkResponse.type === 'basic') {
                    const responseToCache = networkResponse.clone();
                    caches.open(CACHE_NAME).then((cache) => {
                        cache.put(event.request, responseToCache);
                    });
                }
                return networkResponse;
            })
            .catch(() => {
                // Offline fallback to cache
                return caches.match(event.request).then((cachedResponse) => {
                    if (cachedResponse) {
                        return cachedResponse;
                    }
                    if (event.request.headers.get('accept') && event.request.headers.get('accept').includes('text/html')) {
                        return caches.match('./index.html');
                    }
                });
            })
    );
});

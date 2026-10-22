#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Her Şeyi Çay Gibi Demleyen Algoritma
=====================================
Bu algoritma, verdiğiniz herhangi bir şeyi (kavram, nesne, duygu, politika vs.)
çay demler gibi demler. Gerçekten çalışır. Deneyin.

Kullanım: python demle.py "demlenecek şey"
"""

import sys
import time
import random

def demle(sey):
    print("🍵 Demleme süreci başlıyor...")
    time.sleep(1)
    print(f"Su ısıtılıyor... {sey} için ideal sıcaklık hesaplanıyor.")
    time.sleep(1.5)
    
    adimlar = [
        "Yapraklar (metaforik) ıslatılıyor...",
        "İlk demleme turu: 30 saniye...",
        "İkinci demleme: Derinlik kazanıyor...",
        "Aroma açığa çıkıyor... (veya çıkmıyor)",
        "Son süzgeç: Absürtlük filtresi uygulandı."
    ]
    
    for adim in adimlar:
        print(adim)
        time.sleep(random.uniform(0.8, 1.8))
    
    sonuclar = [
        f"{sey} artık mükemmel demlenmiş durumda. İçilebilirlik: %{random.randint(42, 99)}",
        f"{sey} demlendi. Yan etkisi: Varlıksal kriz veya keyif. İkisinden biri.",
        f"Demleme tamam. {sey} artık çaydanlıkta yaşıyor. Onu rahatsız etmeyin.",
        f"{sey} demlendi ama biraz acı oldu. Şeker eklemeyi düşünün. Veya düşünmeyin."
    ]
    
    print("\n" + random.choice(sonuclar))
    print("\nAfiyet olsun. Ya da olmasın. Bu sizin tercihiniz.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python demle.py 'demlenecek şey'")
        print("Örnek: python demle.py 'varoluş' ")
        sys.exit(1)
    
    sey = " ".join(sys.argv[1:])
    demle(sey)

# Gizli not: Bazen en iyi demlemeler en beklenmedik yerlerde olur. 
# (Burada gizli bir şey yok, ya da var. Kim bilir.)

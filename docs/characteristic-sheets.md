---
title: The Ordnance Survey Characteristic Sheets — our extraction
description: OS writing categories, exemplars, letterforms, and Getty AAT mappings
---

# The Ordnance Survey Characteristic Sheets

The Ordnance Survey published **"Characteristic Sheets"** — reference keys to the lettering it used on
its maps. GB-STAMP is grounded in the sheet
**["Examples for the Characters of the Writing on the Engraved Six-Inch Ordnance Maps of Great Britain" (1897)](https://maps.nls.uk/view/128076792)**,
digitised by the **National Library of Scotland** (reproduced under CC-BY), together with the later
(c. 1923) revision.

These sheets are the Rosetta Stone of the project: they record the Ordnance Survey's *own* rule that
**the style of the lettering encodes the kind of feature**. Two points are worth emphasising because they
do a lot of work in the method:

- **Administrative levels are distinguished by different ALL-CAPITALS and fancy faces.** Counties,
  divisions of counties, hundreds, ancient parishes, civil parishes/townships, liberties, boroughs and wards
  are *not* all set the same way — each rung of the administrative hierarchy has its own capital or
  decorated letterform, so the typography alone signals *which level of jurisdiction* a name belongs to.
- **The convention changed in 1879.** Names marked † on the sheet were lettered one way before 1879 and
  differently after, so the style→type mapping is **edition-dependent**: we key each label to its sheet's
  publication date.

Below is our machine-readable extraction of the sheet — the categories, an exemplar clipped from the sheet
itself, the letterform we assign, the date regime, and the Getty **Art & Architecture Thesaurus** term the
category maps to. AAT mappings are still being finalised; cells marked *in progress* are not yet resolved.

<style>
.cs-table { border-collapse: collapse; width: 100%; font-size: 14px; }
.cs-table td, .cs-table th { border: 1px solid #ddd; padding: 6px 8px; vertical-align: middle; text-align: left; }
.cs-table th { background: #f4f4f4; }
.cs-table tr:nth-child(even) { background: #fafafa; }
.muted { color: #888; font-size: 12px; }
</style>

<table class="cs-table">
<thead><tr><th>Exemplar</th><th>Category</th><th>Group</th><th>Letterform</th><th>Date regime</th><th>Getty AAT</th></tr></thead>
<tbody>
<tr><td><img loading="lazy" src="assets/exemplars/ex_boroughs_munic.jpg" alt="Boroughs (Municipal)" style="max-height:34px"></td><td><b>Boroughs (Municipal)</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300000778">boroughs</a><br><span class="muted">aat:300000778</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_boroughs_parl.jpg" alt="Boroughs (Parliamentary)" style="max-height:34px"></td><td><b>Boroughs (Parliamentary)</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300000778">boroughs</a><br><span class="muted">aat:300000778</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_cities_nomp.jpg" alt="Cities not returning Members" style="max-height:34px"></td><td><b>Cities not returning Members</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_cities_nomp.jpg" alt="Cities returning Members" style="max-height:34px"></td><td><b>Cities returning Members</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_civil_parishes.jpg" alt="Civil Parishes or Townships" style="max-height:34px"></td><td><b>Civil Parishes or Townships</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300387092">parishes</a><br><span class="muted">aat:300387092</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_county_boroughs.jpg" alt="County Boroughs" style="max-height:34px"></td><td><b>County Boroughs</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">‡ post-1879 (more recent maps)</td><td><a href="http://vocab.getty.edu/page/aat/300000778">boroughs</a><br><span class="muted">aat:300000778</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_county_names.jpg" alt="County Names" style="max-height:34px"></td><td><b>County Names</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300000771">counties</a><br><span class="muted">aat:300000771</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Divisions of Counties (Ridings)</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Divisions of Townships</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_extra_parochial.jpg" alt="Extra Parochial" style="max-height:34px"></td><td><b>Extra Parochial</b></td><td>admin</td><td>Upright roman</td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_hundreds.jpg" alt="Hundreds" style="max-height:34px"></td><td><b>Hundreds</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_liberties.jpg" alt="Liberties" style="max-height:34px"></td><td><b>Liberties</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_market_towns.jpg" alt="Market Towns" style="max-height:34px"></td><td><b>Market Towns</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><a href="http://vocab.getty.edu/page/aat/300008423">market towns</a><br><span class="muted">aat:300008423</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_other_towns.jpg" alt="Other Towns" style="max-height:34px"></td><td><b>Other Towns</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_parishes_ancient.jpg" alt="Parishes (Mother or Ancient)" style="max-height:34px"></td><td><b>Parishes (Mother or Ancient)</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><a href="http://vocab.getty.edu/page/aat/300387092">parishes</a><br><span class="muted">aat:300387092</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Parliamentary Division of Counties</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">‡ post-1879 (more recent maps)</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_poor_law_unions.jpg" alt="Poor Law Unions" style="max-height:34px"></td><td><b>Poor Law Unions</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Subdivisions of Townships</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_town_districts.jpg" alt="Town Districts" style="max-height:34px"></td><td><b>Town Districts</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">‡ post-1879 (more recent maps)</td><td><a href="http://vocab.getty.edu/page/aat/300008423">market towns</a><br><span class="muted">aat:300008423</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_towns_generally.jpg" alt="Towns, generally" style="max-height:34px"></td><td><b>Towns, generally</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_turnpike_trusts.jpg" alt="Turnpike Trusts" style="max-height:34px"></td><td><b>Turnpike Trusts</b></td><td>admin</td><td>Upright roman</td><td class="muted">† pre-1879</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_urban_sanitary.jpg" alt="Urban Sanitary Districts" style="max-height:34px"></td><td><b>Urban Sanitary Districts</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_wards.jpg" alt="Wards" style="max-height:34px"></td><td><b>Wards</b></td><td>admin</td><td>Upright <b>CAPS</b></td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_other_villages.jpg" alt="Other Villages" style="max-height:34px"></td><td><b>Other Villages</b></td><td>settlement</td><td>Upright roman</td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_navigable_rivers_word.jpg" alt="Navigable Rivers and Canals" style="max-height:34px"></td><td><b>Navigable Rivers and Canals</b></td><td>water</td><td>Italic</td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_small_rivers.jpg" alt="Small Rivers &amp; Brooks" style="max-height:34px"></td><td><b>Small Rivers &amp; Brooks</b></td><td>water</td><td>Italic</td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Antiquities: Norman or Subsequent</b></td><td>antiquity</td><td>gothic_blackletter</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300387092">parishes</a><br><span class="muted">aat:300387092</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Antiquities: Pre-historic or Saxon</b></td><td>antiquity</td><td>gothic_blackletter</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300387092">parishes</a><br><span class="muted">aat:300387092</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Antiquities: Roman</b></td><td>antiquity</td><td>gothic_blackletter</td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Bays and Harbours</b></td><td>coastal_water</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300008678">harbors</a><br><span class="muted">aat:300008678</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_bogs_moors_word.jpg" alt="Bogs, Moors and Forests" style="max-height:34px"></td><td><b>Bogs, Moors and Forests</b></td><td>land</td><td>Upright roman · size-variable</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300386886">moors (landforms)</a><br><span class="muted">aat:300386886</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_chapelries.jpg" alt="Chapelries, Other Churches" style="max-height:34px"></td><td><b>Chapelries, Other Churches</b></td><td>settlement_building</td><td>Upright roman</td><td class="muted">† pre-1879</td><td><a href="http://vocab.getty.edu/page/aat/300004590">chapels (rooms or structures)</a><br><span class="muted">aat:300004590</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>County Bridges, Trust Bridges and Others, Isolated Houses</b></td><td>building_structure</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300007836">bridges (built works)</a><br><span class="muted">aat:300007836</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_gentlemens_seats.jpg" alt="Gentlemen&#x27;s Seats" style="max-height:34px"></td><td><b>Gentlemen&#x27;s Seats</b></td><td>building</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300005567">country houses</a><br><span class="muted">aat:300005567</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_manufactories.jpg" alt="Manufactories, Mines, Farms, Locks" style="max-height:34px"></td><td><b>Manufactories, Mines, Farms, Locks</b></td><td>building_industry</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300000206">farms</a><br><span class="muted">aat:300000206</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Other Stations</b></td><td>railway</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300007783">railroad stations</a><br><span class="muted">aat:300007783</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_parish_churches.jpg" alt="Parish Churches &amp; Villages" style="max-height:34px"></td><td><b>Parish Churches &amp; Villages</b></td><td>settlement_building</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300007466">churches (buildings)</a><br><span class="muted">aat:300007466</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Parks and Demesnes</b></td><td>land</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300159932">educational parks</a><br><span class="muted">aat:300159932</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Principal Stations</b></td><td>railway</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300007783">railroad stations</a><br><span class="muted">aat:300007783</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_railways_mineral.jpg" alt="Railways (Mineral)" style="max-height:34px"></td><td><b>Railways (Mineral)</b></td><td>railway</td><td>Italic</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300386657">railroads (administrative)</a><br><span class="muted">aat:300386657</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_railways_passenger.jpg" alt="Railways (Passenger)" style="max-height:34px"></td><td><b>Railways (Passenger)</b></td><td>railway</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300386657">railroads (administrative)</a><br><span class="muted">aat:300386657</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_ranges_hills.jpg" alt="Ranges of Hills (Separate parts / Single Features)" style="max-height:34px"></td><td><b>Ranges of Hills (Separate parts / Single Features)</b></td><td>landform</td><td>Upright roman · size-variable</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300008777">hills (landforms)</a><br><span class="muted">aat:300008777</span></td></tr>
<tr><td><span class="muted">—</span></td><td><b>Woods and Copses</b></td><td>land</td><td>Upright roman</td><td class="muted">any edition</td><td><span class="muted">— (in progress)</span></td></tr>
<tr><td><img loading="lazy" src="assets/exemplars/ex_workhouses.jpg" alt="Workhouses" style="max-height:34px"></td><td><b>Workhouses</b></td><td>building</td><td>Upright roman</td><td class="muted">any edition</td><td><a href="http://vocab.getty.edu/page/aat/300006490">workhouses (buildings)</a><br><span class="muted">aat:300006490</span></td></tr>
</tbody>
</table>

*Exemplar strips are clipped from the NLS scan of the 1897 Characteristic Sheet (CC-BY). 44 categories extracted.*

[← Back to the methodology](index.md)

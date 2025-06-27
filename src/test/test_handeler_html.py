import unittest
import inspect
from src.handeler_html import markdown_to_html_node

class test_handeler_html(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )
    def test_fulltext_allinone(self):
        md = """
# My Grand Adventure Log

This is a **simple paragraph** to start things off. It also has some _italic_ text and a piece of `code_snippet()`.

## Chapter 1: The Mysterious Forest

### A Deep, Dark Place

> "Beware the Whispering Willows," whispered the old hermit.
> "Their roots run deep, and their secrets deeper still."

### Strange Discoveries

- Found a shimmering **blue** mushroom.
- Heard a peculiar bird song.
- Noticed ancient symbols carved into trees:

- First symbol: `circle`
- Second symbol: `triangle`
- Third symbol: `square`

### The Path Less Traveled

1.  Follow the mossy stones.
2.  Cross the bubbling brook.
3.  Ascend the **Screaming** Peak.

1.  Pack warm clothes.
2.  Bring extra ropes.

#### A Glimmer of Hope

We saw a faint light in the distance. It looked like a small `campfire`.

> "Could it be a friend?" I wondered aloud.
```function lightFire() {
console.log("Fire started!");
}
lightFire();```

###### End of Log Entry

This is another paragraph just to ensure multi-paragraph handling is correct. It's a very *long* paragraph that wraps around a bit to test that too. What a journey!
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        expected = """<div><h1>My Grand Adventure Log</h1><p>This is a <b>simple paragraph</b> to start things off. It also has some <i>italic</i> text and a piece of <code>code_snippet()</code>.</p><h2>Chapter 1: The Mysterious Forest</h2><h3>A Deep, Dark Place</h3><blockquote> "Beware the Whispering Willows," whispered the old hermit.
 "Their roots run deep, and their secrets deeper still."</blockquote><h3>Strange Discoveries</h3><ul><li>Found a shimmering <b>blue</b> mushroom.</li><li>Heard a peculiar bird song.</li><li>Noticed ancient symbols carved into trees:</li></ul><ul><li>First symbol: <code>circle</code></li><li>Second symbol: <code>triangle</code></li><li>Third symbol: <code>square</code></li></ul><h3>The Path Less Traveled</h3><ol><li> Follow the mossy stones.</li><li> Cross the bubbling brook.</li><li> Ascend the <b>Screaming</b> Peak.</li></ol><ol><li> Pack warm clothes.</li><li> Bring extra ropes.</li></ol><h4>A Glimmer of Hope</h4><p>We saw a faint light in the distance. It looked like a small <code>campfire</code>.</p><p>> "Could it be a friend?" I wondered aloud. <code>function lightFire() { console.log("Fire started!"); } lightFire();</code></p><h6>End of Log Entry</h6><p>This is another paragraph just to ensure multi-paragraph handling is correct. It's a very *long* paragraph that wraps around a bit to test that too. What a journey!</p></div>"""
        self.assertEqual(html,expected)
         
        
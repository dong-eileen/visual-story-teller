from markdown.inlinepatterns import InlineProcessor
from markdown.util import etree
from markdown.extensions import Extension

class NameTagPattern(InlineProcessor):
    def handleMatch(self, m, data):
        print("Data: " + str(data))
        print("Match: " + str(m))
        name = m.group(1)
        print("Name: " + name)
        newEl = etree.Element('a')
        newEl.set("class", "name-tag")
        newEl.text = name
        return newEl, m.start(0), m.end(0)

class VisualStoryTellerExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.inlinePatterns.register(NameTagPattern(r"{(\S+)} .+", md), "NameTagPattern", 175)
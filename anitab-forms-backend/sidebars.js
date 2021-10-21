module.exports = {
    docs: [
      {
        type: "doc",
        id: "Home",
      },
      {
        type: 'link',
        label: 'AnitaB.org', 
        href: 'https://anitab.org/'
      },
      {
        type: "doc",
        id: "About-AnitaB.org-Open-Source",
      },
      {
        type: "doc",
        id: "Getting-Started",
      },
      {
        type:"category",
        label:"How to Contribute",
        items:[
          {
            type: "doc",
            id:"Commit-Message-Style-Guide",
          },
          {
            type: "doc",
            id: "Quality-Assurance-Test-Cases",
          },
          {
            type: "doc",
            id: "Maintainer-Guidelines",
          },
        ]
      },
      {
        type:"category",
        label:"Documentation",
        items:[
          {
            type:"link",
            label:"Project Requirements",
            href:"https://docs.google.com/document/d/1xl9F5kMZrKo4mNhnP0SKpk7WkQc8PLca1ym7EZMpjSc/edit"
          },
          {
            type:"category",
            label:"Setup and Install",
            items:[ {
              type: "doc",
              id: "Fork,-Clone,-Remote-and-Pull-Request",
            },
            {
              type: "doc",
              id:"Export-Environment-Variables",
            }]
          },
          {
            type:"category",
            label:"Development",
            items:[ 
          {
            type: "doc",
            id: "Tech-Stack",
          },
          {
            type: "doc",
            id: "Coding-Standards"
          },
          {
            type: "doc",
            id: "Technical-Decisions",
          },
          {
            type: "doc",
            id: "Code-Organization",
          },
          {
            type: "doc",
            id: "User-Authentication",
          }]
          },
          {
            type: "doc",
            id: "Database-Design"
          },     
          {
            type:"category",
            label:"Initial Docs",
            items:[{
              type: 'link',
              label: 'Backend Documentation',
              href: 'https://documenter.getpostman.com/view/11324046/Szzoaw1q'
            }]
          },
          {
            type: "doc",
            id: "Main-Concepts",
          },
          {
            type: "doc",
            id: "Forms",
          },
          {
            type: "doc",
            id: "Automation-and-Filtering",
          },
          {
            type: "doc",
            id: "Future-Ideas",
          },
        ]
      },
      {
        type: 'doc',
        id: 'GSoC-All-Final-Reports', 
      },
      {
        type:"category",
        label:"GSoC Students",
        items:[{
          type: "doc",
          id: "2020-Bismita-Guha",
        }]
      }
    ],
};

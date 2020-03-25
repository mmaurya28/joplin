from gql import gql

queries = {
    'topiccollection': gql('''
    query getTopicCollectionPageRevision($id: ID) {
      allPageRevisions(id: $id) {
        edges {
          node {
            asTopicCollectionPage {
              title
              slug
              description
              theme {
                slug
                text
                description
              }
            }
          }
        }
      }
    }
    '''),
    'topic': gql('''
        query getTopicPageRevision($id: ID) {
          allPageRevisions(id: $id) {
            edges {
              node {
                asTopicPage {
                  title
                  slug
                  description
                  topiccollections {
                    edges {
                      node {
                        topiccollection {
                          title
                          slug
                          description
                          theme {
                            slug
                            text
                            description
                          }
                          liveRevision {
                            id
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
    '''),
    'information': gql('''
    query getInformationPageRevision($id: ID) {
      allPageRevisions(id: $id) {
        edges {
          node {
            asInformationPage {
              title
              slug
              description
              topics {
                edges {
                  node {
                    topic {
                      title
                      slug
                      description
                      topiccollections {
                        edges {
                          node {
                            topiccollection {
                              title
                              slug
                              description
                              theme {
                                slug
                                text
                                description
                              }
                              liveRevision {
                                id
                              }
                            }
                          }
                        }
                      }
                      liveRevision {
                        id
                      }
                    }
                  }
                }
              }
              additionalContent
              contacts {
                edges {
                  node {
                    contact {
                      id
                    }
                  }
                }
              }
              coaGlobal
            }
          }
        }
      }
    }
    '''),
    'services': gql('''
    query getServicePageRevision($id: ID) {
      allPageRevisions(id: $id) {
        edges {
          node {
            asServicePage {
              title
              slug
              shortDescription
              dynamicContent
              steps
              topics {
                edges {
                  node {
                    topic {
                      title
                      slug
                      description
                      topiccollections {
                        edges {
                          node {
                            topiccollection {
                              title
                              slug
                              description
                              theme {
                                slug
                                text
                                description
                              }
                              liveRevision {
                                id
                              }
                            }
                          }
                        }
                      }
                      liveRevision {
                        id
                      }
                    }
                  }
                }
              }
              additionalContent
              contacts {
                edges {
                  node {
                    contact {
                      id
                    }
                  }
                }
              }
              coaGlobal
            }
          }
        }
      }
    }
    '''),
}
